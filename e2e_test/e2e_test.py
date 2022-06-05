import multiprocessing
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase

from app import main

DRIVER_PATH = 'chromedriver.exe'
class TestEnd2End(TestCase):
    
    @classmethod
    def setUpClass(inst):
        inst.app_process = multiprocessing.Process(target=main, args=('test_database.db',))
        inst.app_process.start()
        time.sleep(5)
        inst.start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        inst.driver = webdriver.Chrome(chrome_options=chrome_options)
        inst.driver.get('http://localhost:5000/')

    
    def test_register(self):
        pass
        self.driver.get("http://localhost:5000")
        print("Registering")
        register_link = self.driver.find_element(by=By.ID, value='register_link')
        register_link.click()
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        expected_title = 'Todo App'
        result_title = self.driver.find_element(by=By.ID, value='title')
        
        assert expected_title == result_title.text

    def test_login(self):
        pass
        self.driver.get("http://localhost:5000")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        expected_title = 'Todo App'
        result_title = self.driver.find_element(by=By.ID, value='title')
        
        assert expected_title == result_title.text
    
    def test_logout(self):
        self.driver.get("http://localhost:5000")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        print("Logging out")
        logout_button = self.driver.find_element(by=By.ID, value='logout_button')
        logout_button.click()
        expected_title = 'Log-in to your account'
        result_title = self.driver.find_element(by=By.CLASS_NAME, value='content')
        
        assert expected_title == result_title.text

    def test_add_todo(self):
        self.driver.get("http://localhost:5000")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        print("Adding todo")
        todo_input = self.driver.find_element(by=By.ID, value='todo_input')
        todo_input.send_keys('test_todo')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        expected_title = '1 | test_todo'
        result = self.driver.find_element(by=By.CLASS_NAME, value='big')
        
        assert expected_title == result.text
    
    def test_delete_todo(self):
        self.driver.get("http://localhost:5000")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        print("Adding todo")
        todo_input = self.driver.find_element(by=By.ID, value='todo_input')
        todo_input.send_keys('test_todo')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        time.sleep(2)
        print("Deleting todo")
        delete_todo_button = self.driver.find_element(by=By.ID, value='delete_todo_button')
        delete_todo_button.click()
        time.sleep(1)
        result_title = self.driver.find_elements(by=By.CLASS_NAME, value='big')
        
        assert result_title == []
    
    def test_edit_todo(self):
        self.driver.get("http://localhost:5000")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        print("Adding todo")
        todo_input = self.driver.find_element(by=By.ID, value='todo_input')
        todo_input.send_keys('test_todo')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        time.sleep(1)
        print("Editing todo")
        edit_todo_button = self.driver.find_element(by=By.ID, value='update_todo_button')
        edit_todo_button.click()
        time.sleep(2)
        expected_state = 'Completed'
        result = self.driver.find_element(by=By.ID, value='state')
        
        assert result.text == expected_state

    @classmethod
    def tearDownClass(inst):
        inst.end = time.time()
        elapsedtime=inst.end-inst.start
        print("\n-------\nE2E test duration: ", "{:.2f}".format(elapsedtime), "seconds")
        inst.driver.quit()
        inst.app4test_process.terminate()
        os.remove('test_database.db')