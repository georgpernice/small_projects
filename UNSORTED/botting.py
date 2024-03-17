from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://ilias.h-ka.de")

def login(user,pwd):
    
    nameInput = driver.find_element(By.NAME,"username")
    nameInput.clear()
    nameInput.send_keys(user)
    pwdInput = driver.find_element(By.NAME,"password")
    pwdInput.clear()
    pwdInput.send_keys(pwd)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Text in your webpage')]"))).click()
    
    
    
login("georg","XXXXX")
sleep(100)


driver.close()
