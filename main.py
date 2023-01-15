from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from notification import NotificationManager

notification = NotificationManager()
s = Service("your folder place for chromedriver file")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
URL = "https://icp.administracionelectronica.gob.es/icpco/index"
driver.get(URL)


girona = driver.find_element(By.NAME, 'form')
girona.send_keys("Girona")
aceptar = driver.find_element(By.ID, 'btnAceptar')
aceptar.click()
oficina = driver.find_element(By.ID, 'sede')
oficina.send_keys("Adress your police")
tramites = driver.find_element(By.ID, 'tramiteGrupo[0]')
tramites.send_keys("POLICIA - RECOGIDA DE TARJETA DE IDENTIDAD DE EXTRANJERO (TIE)")
aceptar = driver.find_element(By.ID, 'btnAceptar')
aceptar.click()
driver.execute_script("window.scrollBy(0, 1000);")
entrar = driver.find_element(By.XPATH, '//*[@id="btnEntrar"]')
entrar.click()
nie = driver.find_element(By.ID, 'txtIdCitado')
nie.send_keys("Your NIE")
nombre = driver.find_element(By.ID, 'txtDesCitado')
nombre.send_keys("Your  Fist and Second Name")
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
