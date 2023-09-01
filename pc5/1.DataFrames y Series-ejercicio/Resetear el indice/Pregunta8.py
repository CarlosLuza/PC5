# Resetea el índice

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
avengers_fecha = avengers.set_index("fecha_inicio").copy()
avengers_fecha.reset_index(drop=True, inplace=True)
print(avengers_fecha)
