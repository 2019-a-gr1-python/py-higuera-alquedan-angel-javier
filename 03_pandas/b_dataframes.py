#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:37:49 2019

@author: tenshi
"""


import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)

df_rand_1=pd.DataFrame(arr_rand, columns=["estatura (cm)", "peso (gr)", "edad (anios)"])

df_rand_2=pd.DataFrame(arr_rand)

df_rand_2.columns=["estatura (cm)", "peso (gr)", "edad (anios)"]

df_rand_1[0]

df_rand_3=pd.DataFrame(arr_rand)

df_rand_3[0]

df_rand_2["estatura (cm)"]

df_rand_4=pd.DataFrame(arr_rand,
                       columns=["estatura (cm)", "peso (gr)", "edad (anios)"],
                       index=["Adrian", "Vicente"])

df_rand_4["estatura (cm)"]["Adrian"]