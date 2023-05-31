# -*- coding: utf-8 -*-
"""Buscar el índice de un elemento en una lista.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8Upnc7j9MIeTWGBh93VDvfbv60TPRpy

**Reto 5: Buscar el índice de un elemento en una lista**
Escriba una función que reciba una lista y un número entero a buscar, y que retorne un entero que indique el índice en que se encuentra este elemento.

En caso de que el elemento se encuentre más de una vez dentro de la lista, debe retornar la primera posición en que lo encuentre.

En caso de no encontrar el número, retorne -1.

**Nombre de la función: buscar_elemento**
"""

def buscar_elemento(entrada:list, buscado: int)->int:
    buscar = ()
    for index, x in enumerate(entrada):
        if x == buscado:
             buscar = index
             break
        else:
            buscar = -1
        
    return buscar