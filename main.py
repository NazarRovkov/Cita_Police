from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client
from notification import NotificationManager

notification = NotificationManager()
s = Service("/Users/nazar/Documents/Chromedriver/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
URL = "https://icp.administracionelectronica.gob.es/icpco/index"
driver.get(URL)


def send_to_me(event=None, context=None):
    # get your sid and auth token from twilio
    account_sid = 'AC307ab31f694882839233b050bc6c2489'
    auth_token = '370143a1a53f01256df0db424933f9a8'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=TEXT,
        to='whatsapp:+905512000029'

    )


girona = driver.find_element(By.NAME, 'form')
girona.send_keys("Girona")
aceptar = driver.find_element(By.ID, 'btnAceptar')
aceptar.click()
oficina = driver.find_element(By.ID, 'sede')
oficina.send_keys("CNP LLORET DE MAR, VIRGEN DE LORETO, 51")
tramites = driver.find_element(By.ID, 'tramiteGrupo[0]')
tramites.send_keys("POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)")
aceptar = driver.find_element(By.ID, 'btnAceptar')
aceptar.click()
# id="btnEntrar"
driver.execute_script("window.scrollBy(0, 1000);")
entrar = driver.find_element(By.XPATH, '//*[@id="btnEntrar"]')
entrar.click()
nie = driver.find_element(By.ID, 'txtIdCitado')
nie.send_keys("Y9580700H")
nombre = driver.find_element(By.ID, 'txtDesCitado')
nombre.send_keys("Nazar Rovkov")
Enviar = driver.find_element(By.ID, 'btnEnviar')
Enviar.click()
Solicitar_cita = driver.find_element(By.ID, 'btnEnviar')
Solicitar_cita.click()
info = driver.find_element(By.CLASS_NAME, 'mf-msg__info')
print(info.text)
if "En este momento no hay citas disponibles." in info.text:

    TEXT = "Ups, no citas."
    send_to_me()
    print(TEXT)
    notification.telegram_bot_send_text(
    "no citas"
        )

else:
    TEXT = "Police site have s citas!"
    print(TEXT)
    send_to_me()
    notification.telegram_bot_send_text(
    "Police site have s citas!"
        )
