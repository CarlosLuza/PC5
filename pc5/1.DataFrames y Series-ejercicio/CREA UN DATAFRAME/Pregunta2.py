
# Crear un DataFrame vacío
import pandas as pd
df = pd.DataFrame()

# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado

serie_numeros = pd.Series([10, 20, 10])
df['numeros'] = serie_numeros

print(df)