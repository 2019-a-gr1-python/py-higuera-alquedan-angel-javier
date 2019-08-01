#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:23:28 2019

@author: tenshi
"""

import numpy as np
import pandas as pd
import os
import sqlite3

path_guardado = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.pickle'

data_recuperado = pd.read_pickle(path_guardado)

df = data_recuperado.iloc[49980:50019,:].copy()


# Tipos de archivos 
#     - JSON 
#     - Sql
#     - Excel

###################Importacion a excel ######################
df.to_excel('ejemplo_importacion_excel.xls')

df.to_excel('ejemplo_importacion_excel_2.xls', index=False)

columnas = ['artists', 'title', 'year']

df.to_excel('ejemplo_importacion_excel_2.xls', index=False, columns= columnas)

################### multiples worksheets ######################

writer = pd.ExcelWriter('ejemplo_writter.xls', engine= 'xlswritter')

df.to_excel(writer, sheet_name='preview uno')
df.to_excel(writer, sheet_name='preview dos', index=False)
df.to_excel(writer, sheet_name='preview tres', index=False, columns= columnas)

writer.save()

################### formato de celdas ######################

artistas_contados = data_recuperado['artist'].value_counts()

writer_2 = pd.ExcelWriter('colores.xls', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_2, sheet_name='Artistas Contados')

hoja_artistas = writer_2.sheets['Artistas Contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index))

formato = {
  'type': '2_color_scale',
  'min_value': '10',
  'min_type': 'percentile',
  'max_value': '99',
  'max_type': 'percentile'
}

hoja_artistas.conditional_format(rango_celdas, formato)

writer_2.save()

################### SQL ######################

with sqlite3.connect('bdd_python.db') as conexion:
  df.to_sql('alguien', conexion)


################### JSON ######################

df.to_json('artistas.json')
df.to_json('artistas_2.json', orient='table')


################### FORMATTOS EJERCICIO ######################

################### EQUALS TO ######################

artistas_contados = data_recuperado.iloc[49900:50000,:]

writer_3 = pd.ExcelWriter('ejercicio1.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')

workbook  = writer_3.book
hoja_df = writer_3.sheets['df']

rango_celdas = 'E2:E{}'.format(len(artistas_contados.index)+1)
formato = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})
condicion = {'type':     'cell',
           'criteria': 'equal to',
           'value':     1983,
           'format':    formato
}

hoja_df.conditional_format(rango_celdas, condicion)
writer_3.save()

################### DATA BAR ######################

artistas_contados = data_recuperado.iloc[49900:50000,:]
artistas_contados['width']=artistas_contados['width'].apply(lambda x: int(x))
artistas_contados['height']=artistas_contados['height'].apply(lambda x: int(x))
artistas_contados['total']=artistas_contados['width']*artistas_contados['height']

artistas_contados=artistas_contados.sort_values(by=['total'], ascending=False)

writer_3 = pd.ExcelWriter('ejercicio2.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')

hoja_df = writer_3.sheets['df']

rango_celdas = 'I2:I{}'.format(len(artistas_contados.index)+1)

hoja_df.conditional_format(rango_celdas, { 'type': 'data_bar',
                                           'bar_color': '#63C384',
                                           'bar_solid': True
                                           })
writer_3.save()

################### AVERAGE ######################

writer_3 = pd.ExcelWriter('ejercicio3.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')
workbook  = writer_3.book
hoja_df = writer_3.sheets['df']

rango_celdas = 'I2:I{}'.format(len(artistas_contados.index)+1)
formato1 = workbook.add_format({'bg_color':   '#ff944d'})
formato2 = workbook.add_format({'bg_color':   '#47d147'})

hoja_df.conditional_format(rango_celdas, {'type':     'average',
                                       'criteria': 'above',
                                       'format':   formato2})

hoja_df.conditional_format(rango_celdas, {'type':     'average',
                                       'criteria': 'below',
                                       'format':   formato1})
writer_3.save()

################### DUPLICATE ######################

writer_3 = pd.ExcelWriter('ejercicio4.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')
workbook  = writer_3.book
hoja_df = writer_3.sheets['df']

rango_celdas = 'I2:I{}'.format(len(artistas_contados.index)+1)
formato1 = workbook.add_format({'bg_color':   '#ff944d'})

hoja_df.conditional_format(rango_celdas, {'type':     'duplicate',
                                       'format':   formato1})

writer_3.save()

################### TOP-BOTTOM ######################

writer_3 = pd.ExcelWriter('ejercicio5.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')
workbook  = writer_3.book
hoja_df = writer_3.sheets['df']

rango_celdas = 'I2:I{}'.format(len(artistas_contados.index)+1)
formato1 = workbook.add_format({'bg_color':   '#ff944d'})
formato2 = workbook.add_format({'bg_color':   '#47d147'})
                                
hoja_df.conditional_format(rango_celdas, {'type':     'top',
                                          'value': 5,
                                          'format':   formato2})

hoja_df.conditional_format(rango_celdas, {'type':     'bottom',
                                          'value': 5,
                                          'format':   formato1})

writer_3.save()

################### DATE ######################

writer_3 = pd.ExcelWriter('ejercicio6.xlsx', engine= 'xlsxwriter')
artistas_contados.to_excel(writer_3, sheet_name='df')

workbook  = writer_3.book
hoja_df = writer_3.sheets['df']

rango_celdas = 'E2:E{}'.format(len(artistas_contados.index)+1)
formato = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})
condicion = {'type':     'time_period',
           'criteria': 'last 7 years',
           'format':    formato
}

hoja_df.conditional_format(rango_celdas, condicion)
writer_3.save()