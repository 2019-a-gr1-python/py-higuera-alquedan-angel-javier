#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:14:23 2019

@author: tenshi
"""

print("hola")

nombre="Angel"
edad=27

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]

numeros_serie = pd.Series(lista_numeros)

tupla_numeros=(1,2)

tupla_series = pd.Series(tupla_numeros)

np_array = np.array((1,2,3,4))

np_series = pd.Series(np_array)

numeros_series_1 = pd.Series([
        True,
        False,
        12,
        "Falso",
        12.21,
        None,
        (),
        [],
        {nombre:"Angel"}
        ])

lista_ciudades=["Ambato", "Cuenca", "Loja", "Quito"]

serie_ciudades=pd.Series(lista_ciudades, index=["A", "C", "L", "Q"])

serie_ciudades["Q"]

valores_ciudad={
        "Ibarra": 9500,
        "Guayaquil": 10000,
        "Cuenca":7000,
        "Loja": 3000,
        "Quito": 8000
        }
serie_valor_ciudad=pd.Series(valores_ciudad)

serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]

series_menores=serie_valor_ciudad[serie_valor_ciudad<5000]

series_menores

serie_valor_ciudad=serie_valor_ciudad*1.1

serie_valor_ciudad["Quito"]=8750

print("Lima" in serie_valor_ciudad)

ciudades_uno=pd.Series({
        "Quito": 2000,
        "Loja": 4000
        })
ciudades_dos=pd.Series({
        "Montanita": 2000,
        "Guayaquil": 4000,
        "Quito": 2000
        })

print(ciudades_dos*ciudades_uno)

randomico = np.random.rand(3)
serie_tres_rand=pd.Series(randomico)

ciudades_uno.index

ciudades_tres=pd.Series({
        "Manabi": 2000,
        "Esmeraldas": 4000
        })
# Concatenar series
# Aniadir un indice valor a la sereie
# Maximo 
# Minimo
# Estadisticas (Avg, Mean)
# 
combinado_1=pd.concat([ciudades_uno, ciudades_dos])
combinado_2=pd.concat([ciudades_uno, ciudades_tres])

combinado_1["Quito"]

combinado_3=combinado_1.append(combinado_2)

maximo = ciudades_uno.max
maximo
minimo= ciudades_uno.min
minimo
average= ciudades_uno.mean
average

'''
0 >= 1000 5%
1000 >= 10000 10%
10000 > 15%
'''

ciudades_map=pd.Series({
        "Quito": 200,
        "Loja": 7000,
        "Montanita": 2000,
        "Guayaquil": 12000
        })

ciudades_map_add=ciudades_map.map(lambda x: x+x*0.05 if x<=1000 else x+x*0.10 if x<=10000 else x+x*0.15 )
ciudades_map_add














