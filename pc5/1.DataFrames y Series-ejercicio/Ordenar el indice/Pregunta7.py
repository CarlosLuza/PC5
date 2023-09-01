# Ordena el índice de forma descendiente
import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
avengers_fecha = avengers.set_index("fecha_inicio").copy()
avengers_fecha_sorted = avengers_fecha.sort_index(ascending=False)
print(avengers_fecha_sorted)
