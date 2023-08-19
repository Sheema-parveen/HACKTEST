from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Information import info
from selenium.webdriver.support.ui import Select
from Test_Location import location
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep

#Test_suite
class Test_project:  
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))        
        yield
        self.driver.close()

    def test_get_title(self,startup):
        self.driver.get(info.Info().url)
        assert self.driver.title=="CURA Healthcare Service"
        print("success:correct url")

    def test_make_appointment_login(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        assert self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
        print("SUCCESS: the user is logged in successfully")

    def test_appointment(self,startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"):
          #select_by_value in dropdown
          facility = self.driver.find_element(by=By.ID, value=location.Location.facility)
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
          assert self.driver.find_element(by=By.ID, value=location.Location().book_appointment).click()
          print("appointment booked")
          
    def test_profile(self,startup):
        if(self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"):
           self.driver.find_element(by=By.ID, value=location.Location().menu).click()
           prof = self.driver.find_element(by=By.XPATH, value=location.Location.profile)
           action = ActionChains(self.driver)
           action.click(on_element=prof).perform()
           print("profile shown")
           sleep(3)
           self.driver.find_element(by=By.XPATH, value=location.Location.proflog).click()
           assert  self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/"