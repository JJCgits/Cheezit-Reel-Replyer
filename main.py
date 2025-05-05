from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC


#constants
Username = "jjcheezit"
InstaUNID = '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'

Password = "jjc11905535"
InstaPID = '//*[@id="loginForm"]/div[1]/div[2]/div/label/input'

loginButtonID = '//*[@id="loginForm"]/div[1]/div[3]/button'

dmButtonID = '//*[@id="mount_0_0_7C"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div'



driver = webdriver.Chrome()


def login():
    driver.get("https://www.instagram.com/")
    actions = ActionChains(driver)
    time.sleep(9)

    UNbutton = driver.find_element(By.XPATH, InstaUNID)
    UNbutton.send_keys(Username)

    InstaPB = driver.find_element(By.XPATH, InstaPID)
    InstaPB.send_keys(Password)

    loginButton = driver.find_element(By.XPATH, loginButtonID)
    loginButton.click()

    time.sleep(6)

    for x in range(23):
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.7)

    actions.send_keys(Keys.ENTER).perform()

    time.sleep(3)
    
    for x in range(2):
        actions.send_keys(Keys.TAB).perform()
        time.sleep(0.7)
    
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(60)

    


def recieveDM():
    pass

def runAll():
    pass

def runDM():
    pass

login()