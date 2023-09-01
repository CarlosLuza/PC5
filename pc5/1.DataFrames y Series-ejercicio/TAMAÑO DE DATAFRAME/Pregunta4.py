# Muestra el tamaño del DataFrame

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
print(avengers.shape)
