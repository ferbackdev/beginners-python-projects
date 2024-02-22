import smtplib
import ssl
from email.message import EmailMessage
import configparser


# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
email_sender = config['Email']['email_sender']
email_password = config['Email']['email_password']

email_receiver = 'fernandalippolis@yahoo.com'

msg = EmailMessage()
msg['Subject'] = 'Teste de envio de email'
msg['From'] = email_sender
msg['To'] = email_receiver
body = 'Teste de envio de email'
msg.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, msg.as_string())

print('Email enviado com sucesso!')