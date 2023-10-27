import stomp
import random
import time
from faker import Faker

# Inicializa el generador de datos ficticios
fake = Faker()

# Configuración de la conexión a ActiveMQ
conn = stomp.Connection([('localhost', 61613)])
conn.connect()

# Función para simular el envío de correo electrónico con datos aleatorios
def send_random_email():
    sender = fake.email()
    recipient = fake.email()
    subject = fake.sentence()
    body = fake.paragraph()

    email_data = {
        "remitente": sender,
        "destinatario": recipient,
        "asunto": subject,
        "cuerpo": body
    }

    # Publica el mensaje en la cola de correo electrónico
    conn.send(body=str(email_data), destination='/queue/EmailQueue')

    print(f"Correo electrónico enviado: De: {sender}, Para: {recipient}, Asunto: {subject}")

while True:
    send_random_email()

    # Simula una eventualidad aleatoria de fallo y reintentos
    if random.random() < 0.1:  # Simula un 10% de fallos
        print("Fallo al enviar el correo. Se reintentará más tarde.")
        time.sleep(random.randint(30, 60))  # Espera antes de reintentar
    else:
        time.sleep(random.randint(5, 10))  # Espera entre envíos

conn.disconnect()
