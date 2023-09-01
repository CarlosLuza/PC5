# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv',sep=",")
print(avengers.head())
