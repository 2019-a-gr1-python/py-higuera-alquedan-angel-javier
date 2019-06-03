#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:34:27 2019

@author: tenshi
"""


import numpy as np
import pandas as pd
import os

path_json = '/home/tenshi/xprogramacion/zProgramacion/py-higuera-alquedan-angel-javier/03_pandas/pandas-fundamentals/02/demos/demos/collection-master/artworks'

archivo = '/a/000/a00001-1035.json'

llaves = ['id', 'all_artists', 'title', 'medium', 'dateText', 'acquisitionYear', 'height', 'width', 'units']

path_archivo = path_json + archivo 

with open(path_archivo) as texto_json:
    contenido_json = json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)

