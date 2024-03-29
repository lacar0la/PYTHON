# -*- coding: utf-8 -*-
"""Mejores_ estudiantes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IrQEjI-w1g50_DLm9pG2mgBGM0qQPaKa
"""

import pandas as pd 
import numpy as np

data = np.array([['Nombre', 'matematicas', 'ingles', 'ciencias', 'literatura', 'arte'],
                 ['andrea',2.5, 2.5 , 2.5, 2.5, 2.5],
                 ['andres', 3, 3 , 3, 3, 3],
                 ['camilo',5, 5 , 5, 5, 5],
                 ['Diego',4, 4 , 4, 4, 4],
                 ['pedro',3.5, 4.5 , 3.5, 3.5, 3.5],
                 ['juan',5, 5 , 1, 1, 1],
                 ['Laura',1, 1 , 1, 1, 1],
                 ['Laura',2.5, 4.5 , 4.5, 4.5, 4.5],
                 ['Raul',5, 5 , 5, 5, 5],
                 ['Dani',5, 5 , 5, 5, 5],
                 ['camila',5, 5 , 5, 5, 5],
                 ['Miguel',4, 4 , 4, 4, 4],
                 ['juan',3.5, 4.5 , 3.5, 3.5, 3.5],
                 ['Manolo',5, 5 , 1, 1, 1],
                 ['Pablo',1, 1 , 1, 1, 1],
                 ['Leonardo',2.5, 4.5 , 4.5, 4.5, 4.5],])

estudiantes = pd.DataFrame(data=data[1:,1:],
             index = data[1:,0],
             columns=data[0,1:])

estudiantes["matematicas"]=estudiantes["matematicas"].astype(float)
estudiantes["ingles"]=estudiantes["ingles"].astype(float)
estudiantes["ciencias"]=estudiantes["ciencias"].astype(float)
estudiantes["literatura"]=estudiantes["literatura"].astype(float)
estudiantes["arte"]=estudiantes["arte"].astype(float)

estudiantes= estudiantes.reset_index()

estudiantes.columns =['nombre','matematicas','ingles','ciencias','literatura','arte']

estudiantes

def mejores_estudiantes(estudiantes:pd.DataFrame)->pd.DataFrame:
  copia = estudiantes.copy()
  copia['promedio'] = estudiantes.loc[:, ["matematicas","arte","ingles","ciencias","literatura"]].mean(axis=1)
  copia= copia.drop(["matematicas",'ingles', 'ciencias', 'literatura', 'arte'],axis=1)
  copia = copia.sort_values("promedio", ascending = False)
  num_filas = int(len(copia)*0.25)
  copia = copia.head(num_filas)
  return(copia)

mejores_estudiantes(estudiantes)