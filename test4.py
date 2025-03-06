from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Benutzeranmeldung (NICHT im Code speichern, sondern als Umgebungsvariable)
USERNAME = "dashboard_its@solutec.de"
PASSWORD = "E6SmH#iNNw39d6Nif"

# Pfad zum ChromeDriver (prüfe, ob dieser Pfad korrekt ist)
CHROMEDRIVER_PATH = "/home/solutec/Downloads/chromedriver-linux64/chromedriver"

# Webdriver starten
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximiert das Fenster

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://ww18.autotask.net/")

try:
    # Warte auf das Laden des Login-Felds
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zbce6721329464f8f817e1649d9b6d8e3"))
    )
    username_field.send_keys(USERNAME)
    username_field.send_keys(Keys.RETURN)

    # Warte auf das Passwortfeld
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password_field_id"))
    )
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Warte, bis die Seite geladen ist und überprüfe den Titel
    WebDriverWait(driver, 10).until(EC.title_contains("Autotask"))
    print(f"Login erfolgreich! Seitentitel: {driver.title}")

except Exception as e:
    print(f"Fehler: {e}")

finally:
    time.sleep(5)  # Lasse Zeit, um den Erfolg zu überprüfen
    driver.quit()
