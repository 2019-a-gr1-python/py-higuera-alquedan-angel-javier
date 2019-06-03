#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:41 2019

@author: tenshi
"""

import numpy as np
import pandas as pd
import os

path_guardado = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

section_df = df.iloc[49980:50000,:].copy()

df_agrupado_ay = section_df.groupby('acquisitionYear')

for a, b in df_agrupado_ay:
    print(a)
    
def llenar_valores_vacios(series):
    valores = series.value_count()
    if(valores.empty):
        return series
    nuevo_valor = series