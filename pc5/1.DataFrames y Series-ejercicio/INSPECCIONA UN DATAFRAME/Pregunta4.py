
# Muestra las primeras 5 filas del DataFrame.

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
print(avengers.head())
