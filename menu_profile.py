from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Location import location
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Cura:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def make_appointment_login(self):
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"):
            print("the user is logged in successfully")

    def appointment(self):
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"):
          #select_by_value in dropdown
          facility = self.driver.find_element(by=By.ID, value=location.Location.facility_id)
          facility_dropdown = Select(facility)
          facility_dropdown.select_by_value("Hongkong CURA Healthcare Center")
          #checkbox selection
          self.driver.find_element(by=By.ID, value=location.Location().apply_readmission).click()
          #radio button
          self.driver.find_element(by=By.ID, value=location.Location().medicaid).click()
          #date
          self.driver.find_element(by=By.ID,value=location.Location().visit_date).send_keys(info.Info().visitdate)
          #comment
          self.driver.find_element(by=By.ID,value=location.Location().comment_box).send_keys(info.Info().comment)
          #submit button
          self.driver.find_element(by=By.ID, value=location.Location().book_appointment).click()
          print("appointment booked successfully")

    def profile(self):
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"):
           self.driver.find_element(by=By.ID, value=location.Location().menu).click()
           prof = self.driver.find_element(by=By.XPATH, value=location.Location.profile)
           action = ActionChains(self.driver)
           action.click(on_element=prof).perform()
           print("profile shown")
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=location.Location.proflog).click()
           
    def shutdown(self):
        self.driver.quit()       
           
cura = Cura(info.Info().url)
cura.make_appointment_login()
cura.appointment()
cura.profile()
cura.shutdown()