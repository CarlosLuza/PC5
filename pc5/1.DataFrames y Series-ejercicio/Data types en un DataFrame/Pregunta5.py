# Muestra los data types del dataframe

import pandas as pd
avengers = pd.read_csv('./src/avengers.csv', sep=",")
print(avengers.dtypes)
