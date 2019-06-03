#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:17:45 2019

@author: tenshi
"""

import numpy as np
import pandas as pd
import os

path_guardado = '/home/tenshi/xprogramacion/estudios/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artwork_data.pickle'

data_recuperado = pd.read_pickle(path_guardado)

serie_artistas_duplicados = data_recuperado['artist']

artistas_unicos = pd.unique(serie_artistas_duplicados)

artistas_unicos.size

len(artistas_unicos)

blake = data_recuperado['artist'] == 'Blake, William'

blake.value_counts()

df_blake =  data_recuperado [blake]

df_blake.size