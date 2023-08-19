from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Information import info
from Test_Information import invalid_info
from Test_Location import location
import pytest

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
   
    # invalid login testing
    def test_login1(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(invalid_info.Invalid_info().invalid_username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(invalid_info.Invalid_info().invalid_password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        assert self.driver.current_url != "https://katalon-demo-cura.herokuapp.com/#appointment"
        print(" FAILED: invalid credentials")

    # valid login testing
    def test_make_appointment_login(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID,value=location.Location().make_appointment).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        assert self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
        print("SUCCESS: the user is logged in successfully")

    #login3 : valid login
    def test_toggle_menu_login(self,startup):
        #ANOTHER WAY TO LOGIN
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID,value=location.Location().menu_login).click()
        self.driver.find_element(by=By.XPATH,value=location.Location().login_button2).click()
        self.driver.find_element(by=By.ID,value=location.Location().username_inputbox).send_keys(info.Info().username)
        self.driver.find_element(by=By.ID,value=location.Location().password_inputbox).send_keys(info.Info().password)
        self.driver.find_element(by=By.ID, value=location.Location().login_button).click()
        assert self.driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
        print("the user is logged in successfully")
    