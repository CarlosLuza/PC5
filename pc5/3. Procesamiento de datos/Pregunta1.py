import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

# Cargar el archivo CSV en un DataFrame
candidates_data = pd.read_csv('./src/candidates.csv', sep=";")

# Filtrar los datos según los criterios
filtered_candidates = candidates_data[
    (candidates_data['Seniority'] == 'Mid-Level') &
    (candidates_data['Technology'] == 'Data Engineer') &
    (candidates_data['YOE'] > 2) &
    (candidates_data['Code Challenge Score'] >= 7)
]

# Exportar los candidatos filtrados a un archivo Excel
# Especifica el nombre del archivo de salida
output_filename = './src/candidatos_reporte.xlsx'

filtered_candidates.to_excel(output_filename, index=False)


# Configuración del servidor y credenciales

smtp_server = 'smtp.gmail.com'  # Cambia esto al servidor SMTP que estés utilizando
smtp_port = 587  # Cambia esto al puerto adecuado
sender_email = 'carlosluza1250@gmail.com'
sender_password = "irdoszqqkdlwtpnt" #open('contrasena.txt').read().strip() #'tu_contraseña'

# Detalles del correo electrónico
receiver_email = 'luiguichumbes@gmail.com'
subject = 'Envio Reporte Candidatos'
body = 'Adjunto lo solicitado'

# Crear el objeto MIMEMultipart
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))


# Adjuntar archivo
file_path = './src/candidatos_reporte.xlsx'  # Cambia la ruta al archivo que quieras adjuntar
with open(file_path, 'rb') as file:
    attachment = MIMEApplication(file.read(), _subtype="xlsx")
    attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
    msg.attach(attachment)
    
# Iniciar la conexión con el servidor SMTP
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Iniciar el modo seguro
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Correo enviado exitosamente')
