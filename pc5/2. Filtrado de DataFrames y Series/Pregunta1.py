"""
Caso 1.
Alicia va a ir a Lisboa durante una semana con su marido y sus 2 hijos. Están buscando un apartamento con habitaciones 
separadas para los padres y los hijos. No les importa donde alojarse o el precio, simplemente quieren tener una experiencia agradable. 
Esto significa que solo aceptan lugares con más de 10 críticas con una puntuación mayor de 4. Cuando seleccionemos habitaciones para Alicia, 
tenemos que asegurarnos de ordenar las habitaciones de mejor a peor puntuación. Para aquellas habitaciones que tienen la misma puntuación, 
debemos mostrar antes aquellas con más críticas. Debemos darle 3 alternativas.
"""

import pandas as pd
datos_airbnb = pd.read_csv('./src/airbnb.csv')
habitaciones_filtradas = datos_airbnb[
    (datos_airbnb['bedrooms'] >= 2) & 
    (datos_airbnb['reviews'] > 10) &  
    (datos_airbnb['overall_satisfaction'] > 4) 
]
habitaciones_ordenadas = habitaciones_filtradas.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])
opciones_alicia = habitaciones_ordenadas.head(3)
print(opciones_alicia)
