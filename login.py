#hacktest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Information import invalid_info
from Test_Location import location
from selenium.webdriver.common.by import By

class Cura:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(25)

   #login1: invalid login
    def invalid_login(self):
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(invalid_info.Invalid_info().invalid_username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(invalid_info.Invalid_info().invalid_password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        if(self.driver.current_url != "https://katalon-demo-cura.herokuapp.com/#appointment"):
            print(" invalid credentials")

    #login2 : valid login
    def make_appointment_login(self):
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"):
            print("the user is logged in successfully")


    #login3 : valid  login using toggle
    def toggle_menu_login(self):
    
        #ANOTHER WAY TO LOGIN
        self.driver.find_element(by=By.ID,value=location.Location().menu_login).click()
        self.driver.find_element(by=By.XPATH,value=location.Location().login_button2).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"):
            print("the user is logged in successfully")

    #shutdown
    def shutdown(self):
        self.driver.quit()

#object1: CURA used for invalid login
cura1 = Cura(invalid_info.Invalid_info().url)
cura1.invalid_login()
cura1.shutdown()        

#object2 : CURA used for successful login 
cura = Cura(info.Info().url)
cura.make_appointment_login()
cura.shutdown()

#object3 : CURA used for successful login  using toggle menu
cura2 = Cura(info.Info().url)
cura2.toggle_menu_login()
cura2.shutdown()




