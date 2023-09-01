# Cambia el indice a la columna "fecha_inicio".

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
avengers_fecha = avengers.set_index("fecha_inicio").copy()
print(avengers_fecha)



