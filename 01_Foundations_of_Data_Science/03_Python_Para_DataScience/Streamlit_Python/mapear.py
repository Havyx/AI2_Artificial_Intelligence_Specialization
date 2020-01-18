import pandas as pd
import numpy as np
import streamlit as st

# Codigo de teste para plotar mapa:
#map_data = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [-23.37, -51.28],
#    columns=['lat', 'lon'])
#st.map(map_data)

#Classe para manipular o CSV, apresentando algum erro para converter para DF
class Texto():

    linhas = []
    __dock = []

    def __init__(self):
        file = open('Arquivos/portalbio_export_17-10-2019-13-06-22.csv', 'r')
        self.linhas = file.readlines()

    def construir(self, lines):
        self.__dock = [[item for item in itens.split(';')]for itens in lines]
        return self.__dock

txt = Texto()
#lista = txt.construir(txt.linhas)
#lista = pd.DataFrame(lista[0:][1:], columns=lista[0][0:])
#lista.rename(columns={'Latitude':'lat','Longitude':'lon'}, inplace=True)

mapa_bio = pd.read_csv('Arquivos/mapa_biodiversidade.csv', header=0)

st.deck_gl_chart(
    viewport={
         'latitude': -23.37,
         'longitude': -51.28,
         'zoom': 11,
         'pitch': 50,
     },
     layers=[{
         'type': 'HexagonLayer',
         'data': mapa_bio,
         'radius': 200,
         'elevationScale': 4,
         'elevationRange': [0, 1000],
         'pickable': True,
         'extruded': True,
     }, {
         'type': 'ScatterplotLayer',
         'data': mapa_bio,
     }])

mapa_bio
