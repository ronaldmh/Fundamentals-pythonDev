import requests
from bs4 import BeautifulSoup

# Crear una sesión de navegador
session = requests.Session()

# Iterar a través de un rango de números de cuentas deseadas
for i in range(1,101):
    # Crear una dirección de correo electrónico con el formato "username+número@gmail.com"
    email = "username+" + str(i) + "@gmail.com"
    # Crear una contraseña para la cuenta
    password = "password123"
    # Crear un diccionario con los datos de la cuenta
    data = {"FirstName": "John", "LastName": "Doe", "GmailAddress": email, "Passwd": password, "PasswdAgain": password}
    # Enviar una solicitud POST para crear la cuenta de Gmail
    response = session.post("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp", data=data)
    # Verificar si la cuenta se ha creado correctamente
    if response.status_code == 200:
        print("Cuenta creada con éxito: " + email)
    else:
        print("Error al crear la cuenta: " + email)
