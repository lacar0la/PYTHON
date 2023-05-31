# -*- coding: utf-8 -*-
"""Contar_caracteres_repetidos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IdaxrWakcZsWLVC9_IRT7ZrTEwugHmEc

# Reto 3: Caracteres repetidos

Escriba una función que cuente la cantidad de caracteres diferentes que aparecen más de una vez en una cadena.

Suponga que todas las cadenas se componen únicamente de letras minúsculas del alfabeto en inglés.

   

Su solución debe tener una función de acuerdo con la siguiente especificación:

**Nombre de la función: contar_caracteres_repetidos**

Si lo requiere, puede agregar funciones adicionales.
"""

def contar_caracteres_repetidos(cadena:str)-> int:
    unicos = set(cadena)
    contar = 0
    resultado = 0
    for x in unicos:
        contar = 0
        for j in range (0, len(cadena)):
            if x == cadena[j]:
                contar += 1
                if contar > 1:
                    resultado += 1
                    break         
    return resultado