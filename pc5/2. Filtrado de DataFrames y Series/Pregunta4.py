"""
Caso 1.
Realizar un gráfico circular, de la cantidad de tipo de habitaciones room_type
"""


import pandas as pd
import matplotlib.pyplot as plt
datos_airbnb = pd.read_csv('./src/airbnb.csv', sep=",")
conteo_tipos_habitacion = datos_airbnb['room_type'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(conteo_tipos_habitacion, labels=conteo_tipos_habitacion.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Tipos de Habitación')
plt.axis('equal')  
plt.show()
