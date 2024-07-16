import pandas as pd

import pyautogui
import time
import webbrowser

time.sleep(5)

# url to open
webbrowser.open("https://mail.google.com")

time.sleep(10)

#checking email 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Configuration Webdriver using Edge
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# 
driver.get('https://mail.google.com')

#Wating time
time.sleep(2)

#replace ### by the email
try:
    # Intentar seleccionar una cuenta existente
    account_choice = driver.find_element(By.XPATH, '//div[contains(text(), "######"@gmail.com")]')
    account_choice.click()
except:
    # Si no hay cuenta existente, ingresar el correo electrónico
    email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_field.send_keys('#########@gmail.com')
    email_field.send_keys(Keys.RETURN)

    #wait to the page load
    time.sleep(5)

#  enter email's passwords
password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_field.send_keys('#########')
password_field.send_keys(Keys.RETURN)

# wait a bit to see the mail
time.sleep(20)


# close web
driver.quit()