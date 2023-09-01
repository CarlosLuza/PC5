"""
Caso 3
Diana va a Lisboa a pasar 3 noches y quiere conocer a gente nueva. Tiene un presupuesto de 50€ para su alojamiento. 
Debemos buscarle las 10 propiedades más baratas, dandole preferencia a aquellas que sean habitaciones compartidas (room_type == Shared room), 
y para aquellas viviendas compartidas debemos elegir aquellas con mejor puntuación.
"""


import pandas as pd
datos_airbnb = pd.read_csv('./src/airbnb.csv', sep=",")
presupuesto_maximo = 50
habitaciones_compartidas = datos_airbnb[datos_airbnb['room_type'] == 'Shared room']
propiedades_diana = habitaciones_compartidas[habitaciones_compartidas['price'] <= presupuesto_maximo]
propiedades_ordenadas = propiedades_diana.sort_values(by=['price', 'overall_satisfaction'], ascending=[True, False])
opciones_diana = propiedades_ordenadas.head(10)
print(opciones_diana)
