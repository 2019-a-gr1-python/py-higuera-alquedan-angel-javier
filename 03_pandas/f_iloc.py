#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:36:11 2019

@author: tenshi
"""
import numpy as np
import pandas as pd
import os

path_guardado = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

primero = df.loc[1035]["artist"]

segundo = df.loc[1036, "artist"]

tercero = df.loc[0] # Error por que no se encuentra el indice

primero_a = df.iloc[0,1]

primero_b = df.iloc[0,:]

primero_c = df.iloc[0:100, 0:-2]

tres primeros = df.head(10)['width'].sort_values(axis=0).head(3)

diez_primeros = df['width'].sorting_values(ascending=False).head(10)