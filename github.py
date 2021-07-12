import unittest
import allure
import selenium
from selenium import webdriver  
import time  
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
  
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")
		
    def testLogin(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 

        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)		
	
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
		
class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")
		
    def testRegisterAccount_40(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "1234567890123456789012345678901234567890"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username is too long (maximum is 39 characters). Username " + keys + " is not available."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testRegisterAccount_41(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "12345678901234567890123456789012345678901"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username is too long (maximum is 39 characters)."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testRegisterAccount_dash_begin(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "-"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen. Username " + keys + " is not available."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
	
    def testRegisterAccount_dash_end(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "a-"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
               
        firstValue = element.text
        secondValue = "Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen. Username " + keys + " is not available."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
	
    def testRegisterAccount_double_dash(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "--"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
				
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testRegisterAccount_special_sign(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "#"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testRegisterAccount_polish_letters(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "nameć"
        self.driver.find_element_by_id("user_login").send_keys(keys) 
        time.sleep(3)
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[1]/dl/dd[2]/div/div")
        
        firstValue = element.text
        secondValue = "Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen. Username " + keys + " is not available."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

class MailRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")
		
    def testMailRegister_1_regex_example(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "@a.aa"
        self.driver.find_element_by_id("user_email").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[2]/dl/dd[2]")
        firstValue = element.text
        time.sleep(3) 
        secondValue = "Email is invalid or already taken"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testMailRegister_2_regex_example(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "a@.aa"
        self.driver.find_element_by_id("user_email").send_keys(keys) 
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[2]/dl/dd[2]")
        firstValue = element.text
        secondValue = "Email is invalid or already taken"
        message = "Github unexpectedly allows you to register an email with this address"
        self.assertEqual(firstValue, secondValue, message)
		
    def testMailRegister_3_regex_example(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "a@a.a"
        self.driver.find_element_by_id("user_email").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[2]/dl/dd[2]")
        firstValue = element.text
        time.sleep(3) 
        secondValue = "Email is invalid or already taken"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testMailRegister_unique_address(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "shaidel@wp.pl"
        self.driver.find_element_by_id("user_email").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/auto-check[2]/dl/dd[2]")
        firstValue = element.text
        time.sleep(3) 
        secondValue = "Email is invalid or already taken"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
		
class PasswordRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")
		
    def testPasswordRegister_73_characters(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "1234567890123456789012345678901234567890123456789012345678901234567890123"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password is too long (maximum is 72 characters)"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_popular_numeric_password(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "123456789012345"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password is in a list of passwords commonly used on other websites"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_popular_text_password(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 

        keys = 	"asdfghjklqwerty"	
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password is in a list of passwords commonly used on other websites"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_14_characters_without_number(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = 	"asdfghjklqwert"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password needs at least 1 number and is in a list of passwords commonly used on other websites"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_14_characters_without_letter(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = 	"12345678901234"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 

        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password needs at least 1 lowercase letter and is in a list of passwords commonly used on other websites"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_14_characters_with_lowercase_letters_but_without_number(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "ASDFghjklqwert"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
				
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password needs at least 1 number"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_14_characters_with_numbers_but_without_lowercase_letter(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "12345BARD09876"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password needs at least 1 lowercase letter"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testPasswordRegister_7_characters_with_lowercase_letter_and_number(self):
        self.driver.find_element_by_link_text("Sign up").click()
        time.sleep(3) 
		
        keys = "bard77p"
        self.driver.find_element_by_id("user_password").send_keys(keys) 
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div/form/password-strength/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Password is too short (minimum is 8 characters)"
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
		
class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")
		
    def testSearch_not_find(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_name("q").send_keys("klasdasd") 
        time.sleep(3) 
		
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER) 
        time.sleep(3) 

        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/div/h3")
        time.sleep(3) 
        if "We couldn’t find any repositories matching" in element.text:
            assert True
        else:
            assert False
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testSearch_find(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_name("q").send_keys("asteroids") 
        time.sleep(3) 
		
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER) 
        time.sleep(3) 

        element_repository_results = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/div[1]/h3")
        element_languages = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[2]/div[1]/h2")
        time.sleep(3) 
        if "repository results" in element_repository_results.text and "Languages" in element_languages.text:
            assert True
        else:
            assert False
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

class AddRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/")	
		
    def testAddRepository_name_TATWiN_2021(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_name").send_keys("TATWiN_2021")
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)	
		
    def testAddRepository_name_dash(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_name").send_keys("-")
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)	
		
    def testAddRepository_name_underscore(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_name").send_keys("_")
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)

    def testAddRepository_name_special_sign(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_name").send_keys("`!@#$%^&*()=+[{]}\|;:',<>/?")
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "Your new repository will be created as -."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)			
		
    def testAddRepository_name_101_characters(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        keys = "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901"
        self.driver.find_element_by_id("repository_name").send_keys(keys)
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
                
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = keys + " is available."
        message = "The maximum length of the repository name is 100 characters"
        self.assertEqual(firstValue, secondValue, message)
        
    def testAddRepository_name_e_Indeks(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        keys = "e-Indeks"
        self.driver.find_element_by_id("repository_name").send_keys(keys)
        time.sleep(3) 
		
        element = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd[2]")
        firstValue = element.text
        secondValue = "The repository " + keys +" already exists on this account."
        self.assertEqual(firstValue, secondValue)
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)		

    def testAddRepository_description(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_description").send_keys("Description sample")
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testAddRepository_visibility_public(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_visibility_public").click()
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testAddRepository_visibility_private(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_visibility_private").click()
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testAddRepository_readme(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_auto_init").click()
        time.sleep(3) 
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testAddRepository_gitignore(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_gitignore_template_toggle").click()
        time.sleep(3) 		
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def testAddRepository_licence(self):
        self.driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
        time.sleep(3) 

        self.driver.find_element_by_id("login_field").send_keys("shaidel@wp.pl") 
        time.sleep(3) 

        self.driver.find_element_by_id("password").send_keys("gitBARD77pl") 
        time.sleep(3) 

        self.driver.find_element_by_name("commit").click()
        time.sleep(3) 
		
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("Your repositories").click()
        time.sleep(3) 
		
        self.driver.find_element_by_link_text("New").click()
        time.sleep(3) 
		
        self.driver.find_element_by_id("repository_license_template_toggle").click()
        time.sleep(3) 		
		
        allure.attach(self.driver.get_screenshot_as_png(), name="ScreenshotAdd", attachment_type=AttachmentType.PNG)
		
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()