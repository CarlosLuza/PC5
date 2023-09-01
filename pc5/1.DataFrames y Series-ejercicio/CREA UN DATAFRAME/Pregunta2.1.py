
# Crea otra columna en el dataframe y asignale la segunda Serie que has creado

import pandas as pd
df = pd.DataFrame()
serie_numeros = pd.Series([10, 20, 10])
serie_colores = pd.Series(['rojo', 'verde', 'azul'])
df['numeros'] = serie_numeros
df['colores'] = serie_colores
print(df)


