#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 07:50:32 2019

@author: tenshi
"""

import numpy as np
import pandas as pd
import os

path = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/proyecto/analisis de datos/victimizacion_robo_objetosydemas.csv'

data=pd.read_csv(path)

def listar_ciudades():
    filtered_data = data.loc[:,"NOMBRE"]
    filtered_data = pd.Series.drop_duplicates(filtered_data)
    filtered_data = pd.Series.sort_values(filtered_data)
    print(filtered_data)
    
def ciudades_mayor_incidencia():
    filtered_data = np.copy(data)
    filtered_data = data.groupby(["NOMBRE"]).count()
    filtered_data = filtered_data.iloc[:,1]
    filtered_data = pd.Series.sort_values(filtered_data, ascending=False).head(10)
    print(filtered_data)
    
def numero_incidencias_ciudad(ciudad):
    nombre = ciudad.upper()
    filtered_data = pd.DataFrame.copy(data)
    filtered_data = filtered_data[filtered_data["NOMBRE"]==nombre]
    print(f"Numero de incidencias en {nombre}: {len(filtered_data)}")
    
def numero_incidencias_categoria(ciudad):
    nombre = ciudad.upper()
    filtered_data = pd.DataFrame.copy(data)
    filtered_data = filtered_data[filtered_data["NOMBRE"]==nombre]
    filtered_radio = filtered_data[filtered_data["RO2A101"]==1]
    filtered_muebles = filtered_data[filtered_data["RO2B101"]==1]
    filtered_computador = filtered_data[filtered_data["RO2C101"]==1]
    filtered_tv = filtered_data[filtered_data["RO2B103"]==1]
    filtered_joyas = filtered_data[filtered_data["RO2C103"]==1]
    filtered_celular = filtered_data[filtered_data["RO2C107"]==1]
    filtered_dinero = filtered_data[filtered_data["RO2C105"]==1]
    print(f"Numero de incidencias en {nombre}: {len(filtered_data)}")
    print(f"""Por categoria:
        \tRadio: {len(filtered_radio)}
        \tMuebles: {len(filtered_muebles)}
        \tComputador: {len(filtered_computador)}
        \tTv: {len(filtered_tv)}
        \tJoyas: {len(filtered_joyas)}
        \tCelular: {len(filtered_celular)}
        \tDinero: {len(filtered_dinero)}
        """)

def numero_incidencias_secuestro(ciudad):
    nombre = ciudad.upper()
    filtered_data = pd.DataFrame.copy(data)
    filtered_data = filtered_data[filtered_data["NOMBRE"]==nombre]
    filtered_secuestros = filtered_data[filtered_data["RO61"]==1]
    filtered_secuestros_express = filtered_data[filtered_data["RO61"]==2]
    secuestros = len(filtered_secuestros) + len(filtered_secuestros_express)
    print(f"Numero de secuestros en {nombre}: {secuestros}")
    print(f"""Por categoria:
        \tRescate: {len(filtered_secuestros)}
        \tExpress: {len(filtered_secuestros_express)}
        """)

def iniciar_sistema():
    comando=1
    ciudad="quito"
    while comando!="0":
        print("""Seleccione una opcion:
        \t1) Listar Ciudades
        \t2) Listar 10 Ciudades con mas delitos 
        \t3) Seleccionar ciudad
        \t4) Incidentes por categoria en ciudad
        \t5) Secuestros en ciudad 
        \t0) Salir
        """)
        comando=input("Opcion: ")
        if comando == "1":
            listar_ciudades()
        elif comando == "2":
            ciudades_mayor_incidencia()
        elif comando == "3":
            ciudad=input(f"CIUDAD: {ciudad}")
        elif comando == "4":
            numero_incidencias_categoria(ciudad)
        elif comando == "5":
            numero_incidencias_secuestro(ciudad)

iniciar_sistema()
