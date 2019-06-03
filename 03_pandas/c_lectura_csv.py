#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:54:13 2019

@author: tenshi
"""


import numpy as np
import pandas as pd
import os

path = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.csv'
path_guardado = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.pickle'

data=pd.read_csv(
        path,
        nrows=5,
        usecols=['id', 'artist'],
        index_col='id'
        )

columnas_a_usar=['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width' ]
data_completa=pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id'
        )

data_completa.to_pickle(path_guardado)

data_recuperado = pd.read_pickle(path_guardado)













