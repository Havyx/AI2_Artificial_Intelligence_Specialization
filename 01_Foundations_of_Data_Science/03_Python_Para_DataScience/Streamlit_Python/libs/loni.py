#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:07:01 2019

@author: rafael
"""

# Ex OOP02

from ipyleaflet import Map, Marker
from opencage.geocoder import OpenCageGeocode
#from pprint import pprint
key = "55cd9d801409431c8a15d8b491162ea5"
geocoder = OpenCageGeocode(key)

def teste():
	print('teste')

class TrataCSV:


    # carrega arquivo csv
    def __init__(self, arqv):
        self.arquivo = open(arqv, "r")
        self.lines = []
        self.NoData = []
        self.dataT = []
        return 
    def StripLines(self):
        self.lines = [lines for lines in self.arquivo]
        return self.lines
    def NoDataAverage(self):
        self.dataAux = []
        self.count = 0
        self.data = [data.strip("\n").split(";") for data in self.lines]
        # Lê cada coluna por vez        
        for j in range(len(self.data[0])):        
            for i in range(len(self.data)-1):
                self.dataAux.append(self.data[i][j])
                # Verifica se está sem informação
                if self.data[i][j] == "Sem Informações":
                    self.count += 1
            # Cria uma nova "matriz" de dados transposta
            self.dataT.append(self.dataAux)
            self.NoData.append(self.count/(len(self.data)-2))
            self.dataAux = []
            self.count = 0
        # Calcula a média de elementos vazios nas colunas
        self.mediaNoData = round(sum(self.NoData)/len(self.NoData)*100 , 2)
        print("A média de dados ausentes é {}%.".format(self.mediaNoData))
        return self.NoData
    def TaxoLevel(self):
        self.TaxList = []
        for i in range(len(self.dataT)):
            if self.dataT[i][0] == "Especie":
                for j in range(len(self.dataT[i])):
                    if self.dataT[i][j] != "Sem Informações" :
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Especie"])
                    elif self.dataT[i-1][j] != "Sem Informações" :
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Genero"])
                    elif self.dataT[i-2][j] != "Sem Informações" :
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Familia"])
                    elif self.dataT[i-3][j] != "Sem Informações" :
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Ordem"])
                    elif self.dataT[i-4][j] != "Sem Informações" :
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Classe"])
                    else:
                        self.TaxList.append(["Nível taxonomico de {} é: ".format(j), "Filo"])
        return self.TaxList
    def FilterAmeaca(self, filter01):
        self.AmeacaList = []
        for i in range(len(self.dataT)):
            if self.dataT[i][0] == "Estado de conservacao":
                for j in range(len(self.dataT[i])):
                    if self.dataT[i][j] == filter01 :
                        self.AmeacaList.append(["Amostra {}: {}: ".format(j, self.dataT[i-12][j]), filter01])
        return self.AmeacaList
    def FilterResponsavel(self, filter01):
        self.AmeacaList = []
        for i in range(len(self.dataT)):
            if self.dataT[i][0] == "Responsavel pelo registro":
                for j in range(len(self.dataT[i])):
                    if self.dataT[i][j] == filter01 :
                        self.AmeacaList.append("Responsável pela amostra {}: {}: ".format(j, self.dataT[i+6][j]))
        return self.AmeacaList
    def Location(self):
        # Import pra tratamento das coordenadas
        





        self.results = geocoder.geocode(u'Brussels, Belgium')
        self.center = (self.results[0]['geometry']['lat'], self.results[0]['geometry']['lng'])


        map = Map(center=self.center, zoom=6)
        self.marker = Marker(location = self.center, draggable=False)
        map.add_layer(self.marker)
        map


        
    
        




#arquivo001 = TrataCSV("ex02.csv")
#arquivo001.StripLines()
#arquivo001.NoDataAverage()
#arquivo001.TaxoLevel()
#arquivo001.FilterAmeaca("Espécie Ameaçada")
#arquivo001.FilterResponsavel("Edson Fontes De Oliveira")
#arquivo001.Location()
