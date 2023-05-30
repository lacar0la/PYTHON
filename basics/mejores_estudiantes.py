import pandas as pd 
def mejores_estudiantes(estudiantes:pd.DataFrame)->pd.DataFrame:
  copia = estudiantes.copy()
  copia['promedio'] = estudiantes.loc[:, ["matematicas","arte","ingles","ciencias","literatura"]].mean(axis=1)
  copia= copia.drop(["matematicas",'ingles', 'ciencias', 'literatura', 'arte'],axis=1)
  copia = copia.sort_values("promedio", ascending = False)
  num_filas = int(len(copia)*0.25)
  copia = copia.head(num_filas)
  return(copia)
