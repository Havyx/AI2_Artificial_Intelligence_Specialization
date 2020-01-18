#Importando bibliotecas
import sys
import pandas as pd
import numpy as np
import streamlit as st

#sys.path.append('Bibliotecas')
#from felipe import *
#carregarCSV('Arquivos/portalbio_export_16-10-2019-14-39-54.csv')

class app_hub():

	#Atributos da classe app_hub:
	dicionario = ['Exe. 1: Valores vazios','Exe. 2: Nivel Taxonomico','Exe. 3: Filtros','Exe. 4: Avaliar Lon / Lat']
	linhas = []
	lista_completa = []
	#Metodo construtor
	def __init__(self):
		file = open('Arquivos/portalbio_export_16-10-2019-14-39-54.csv', 'r', encoding='utf8')
		self.linhas = file.readlines()
		st.title('HUB Inteligencia Artificial - Desafio 02')
		if st.sidebar.checkbox('Integrantes'):
			st.sidebar.markdown('#### @Savio')
			st.sidebar.markdown('#### @Felipe')
			st.sidebar.markdown('#### @Lucas')
			st.sidebar.markdown('#### @Rafael')
			st.sidebar.markdown(' ')

	#Metodo para construir a matriz
	def construir(self, lines):
		self.lista_completa = [[item for item in itens.split(',')]for itens in lines]
		return self.lista_completa
	#Metodo para contar os nulos
	def count_nulls(self, lista):
		#list comp que retorna lista das colunas vazias
		def funcao(texto):
			return True if texto == "Sem Informações" or texto == " " else False
		colunas_vazias = [sum([funcao(lista[linha][coluna]) for linha in range(len(lista))]) for coluna in range(len(lista[0]))]
		return colunas_vazias
	#Metodo para retornar a porcetagem de itens sem informação em cada coluna
	def media_nulls(self, lista):
	#Map aplicando a função lambda em cada item da lista
		return map(lambda item: item /len(self.lista_completa), lista)
	#Metodo para checar nível taxonom...
	def taxonom(self):
		count=0
		#Procura pela posição da palavra filo nas colunas:
		for i in range(0, len(self.lista_completa[0:][0])):
			if self.lista_completa[0][i] == 'Filo':
				count = i
				break
		#List comprehension pra criar uma lista com os valores taxon..: 0 a 6
		def testar(teste):
			return False if teste == "Sem Informações" or teste == " " else True
		novas_colunas = [sum([testar(self.lista_completa[linha][coluna]) for coluna in range(count, count+6)]) for linha in range(len(self.lista_completa))]
		novas_colunas.insert(0,'Taxonom')
		return novas_colunas

app = app_hub()

option = st.sidebar.selectbox('Escolha o exercicio: ',app.dicionario)
'Voce selecionou a opcao: ', option

if option == app.dicionario[0]:
	st.write('Para cada coluna identique a quantidade de linhas com dados faltantes (em alguns casos, o dado faltante é uma string vazia, em outros casos é uma string contendo algum valor do tipo: "sem informação"). Faça um método que retorna a média de dados faltantes por coluna')
	st.markdown('### Valores vazios ou faltantes: ')
	st.bar_chart(app.count_nulls(app.construir(app.linhas)))
	if st.checkbox('Mostrar lista de dados faltantes'):
		st.write(app.count_nulls(app.construir(app.linhas)))
	st.markdown('### Porcetagem de valores faltantes por coluna: ')
	st.bar_chart(app.media_nulls(app.count_nulls(app.construir(app.linhas))))
	if st.checkbox('Mostrar lista de porcetagem'):
		st.write(list(app.media_nulls(app.count_nulls(app.construir(app.linhas)))))

if option == app.dicionario[2]:
	mapa_bio = pd.read_csv('Arquivos/mapa_biodiversidade.csv', header=0)
	st.write('Monte filtros de ocorrências por estados, nome de espécie (nome exato ou parte do nome) e categoria de ameaça, e outros filtros que julgar relevante.')
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
		st.dataframe(data)
