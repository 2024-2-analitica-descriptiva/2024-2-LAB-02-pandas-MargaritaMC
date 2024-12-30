"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

# Agregue una columna llamada `suma` con la suma de `c0` y `c2` al data frame
# que contiene el archivo `tbl0.tsv`.
# Rta/
#      c0  c1   c2          c3  suma
# 0     0   E    1  1999-02-28     1
# 1     1   A    2  1999-10-28     3
# ...

import pandas as pd

def pregunta_08():
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df['suma'] = df['c0'] + df['c2']
    print(df)
    return df

pregunta_08()