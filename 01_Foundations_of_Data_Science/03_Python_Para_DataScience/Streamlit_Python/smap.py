#Importando bibliotecas
import pandas as pd
import numpy as np
import streamlit as st

class app_hub():
	#Atributos da classe app_hub:
	dicionario = ['Exe. 1:Valores vazios','Exe. 2:Nivel Taxonomico','Exe. 3:Filtros','Exe. 4:Avaliar lon/lat']

	#Metodo construtor:
	def __innit__(self):
		print('Instancia criada')

	def inicializar_app(self):
		st.title('HUB Inteligencia Artificial - Desafio 02')
		st.sidebar.markdown('## Integrantes: equipe 3')
		st.sidebar.markdown('#### Savio')
		st.sidebar.markdown('#### felipe')
		st.sidebar.markdown('#### Lucas')
		st.sidebar.markdown('#### Rafael')

app = app_hub()
app.inicializar_app()

option = st.sidebar.selectbox('Escolha o exercicio: ',app.dicionario)
'You selected:', option

mapa_bio = pd.read_csv('Arquivos/mapa_biodiversidade.csv', header=0)

if option == 'Exe. 3:Filtros':

	municipios = st.multiselect("Escolha os municipios", list(set(mapa_bio['Municipio'])), ["Londrina"])
	data = mapa_bio.loc[mapa_bio['Municipio'].isin(municipios)]

	st.deck_gl_chart(
    	viewport={
         'latitude': -23.37,
         'longitude': -51.28,
         'zoom': 11,
         'pitch': 50,
     	},
     	layers=[{
         'type': 'HexagonLayer',
         'data': data,
         'radius': 200,
         'elevationScale': 4,
         'elevationRange': [0, 1000],
         'pickable': True,
         'extruded': True,
     	}, {
         'type': 'ScatterplotLayer',
         'data': data,
     	}])

if st.checkbox('Mostrar dados'):
	st.write(data)
