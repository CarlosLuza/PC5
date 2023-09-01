"""
Caso 2
Roberto es un casero que tiene una casa en Airbnb. De vez en cuando nos llama preguntando sobre cuales son las críticas de su alojamiento. 
Hoy está particularmente enfadado, ya que su hermana Clara ha puesto una casa en Airbnb y Roberto quiere asegurarse de que su casa tiene más 
críticas que las de Clara. Tenemos que crear un dataframe con las propiedades de ambos. Las id de las casas de Roberto y Clara son 97503 y 90387 
respectivamente. Finalmente guardamos este dataframe como excel llamado "roberto.xls
"""

import pandas as pd
datos_airbnb = pd.read_csv('./src/airbnb.csv', sep=",")
id_roberto = 97503
id_clara = 90387
propiedades_roberto_clara = datos_airbnb[
    (datos_airbnb['room_id'] == id_roberto) | (datos_airbnb['room_id'] == id_clara)
]
propiedades_roberto_clara.to_excel('roberto.xlsx', index=False)

print("DataFrame guardado como 'roberto.xlsx'")

