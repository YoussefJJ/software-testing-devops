import multiprocessing
import os
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase

from app import main

def deleteUser():
    database_filename = 'db.sqlite'
    connection = sqlite3.connect(database_filename)
    connection.execute(
        "DELETE FROM USER WHERE USERNAME LIKE ?;", ("test_user",))
    connection.commit()
    connection.close()

DRIVER_PATH = 'chromedriver.exe'
class TestEnd2End(TestCase):
    
    @classmethod
    def setUpClass(inst):
        inst.app_process=multiprocessing.Process(target=main,name="App",args=('test_db.db',True,))
        inst.app_process.start()
        time.sleep(5)
        inst.start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        #inst.driver = webdriver.Chrome('chromedriver.exe')
        inst.driver = webdriver.Chrome(options=chrome_options)

        #inst.driver.implicitly_wait(1)
        print("Visiting home page")
        inst.driver.get('http://localhost:5000/')
        inst.driver.save_screenshot('./e2e_test/Screenshots/01_homepage.png')

    
    def test_01_register(self):
        self.driver.get("http://localhost:5000")
        print("Registering")
        register_link = self.driver.find_element(by=By.ID, value='register_link')
        register_link.click()
        self.driver.implicitly_wait(1)
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        self.driver.implicitly_wait(1)
        expected_title = 'To Do App'
        result_title = self.driver.find_element(by=By.ID, value='title')
        
        self.assertEqual(expected_title, result_title.text)

    def test_02_login(self):
        self.driver.get("http://localhost:5000/logout")
        print("Logging in")
        print("fill in form")
        self.driver.implicitly_wait(1)
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        self.driver.implicitly_wait(1)
        expected_title = 'To Do App'
        result_title = self.driver.find_element(by=By.ID, value='title')
        print(result_title)
        # self.driver.implicitly_wait(2)
        self.assertEqual(expected_title, result_title.text)
    
    def test_03_logout(self):
        self.driver.get("http://localhost:5000/logout")
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

    def test_04_add_todo(self):
        self.driver.get("http://localhost:5000/logout")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        self.driver.implicitly_wait(1)
        nb_todos = len(self.driver.find_elements(by=By.CLASS_NAME, value='todo'))
        print("Adding todo")
        todo_input = self.driver.find_element(by=By.ID, value='todo_input')
        todo_input.send_keys('test_todo')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        expected_title = '1 | test_todo'
        result = len(self.driver.find_elements(by=By.CLASS_NAME, value='todo'))
        
        self.assertEqual(result, nb_todos + 1)
    
    def test_05_delete_todo(self):
        self.driver.get("http://localhost:5000/logout")
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
        todo_input.send_keys('test_todo_to_delete')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        time.sleep(2)
        print("Deleting todo")
        delete_todo_button = self.driver.find_elements(by=By.ID, value='delete_todo_button')[-1]
        delete_todo_button.click()
        time.sleep(1)
        result_title = self.driver.find_elements(by=By.XPATH, value='//span[text()="test_todo_to_delete"]')
        
        self.assertEqual(result_title, [])
    
    def test_06_edit_todo(self):
        self.driver.get("http://localhost:5000/logout")
        print("Logging in")
        print("fill in form")
        username_input = self.driver.find_element(by=By.ID, value='nameId')
        username_input.send_keys('test_user')
        password_input = self.driver.find_element(by=By.ID, value='passwdId')
        password_input.send_keys('test_password')
        print("Submitting form")
        submit_button = self.driver.find_element(by=By.ID, value='button')
        submit_button.click()
        self.driver.implicitly_wait(1)
        print("Adding todo")
        todo_input = self.driver.find_element(by=By.ID, value='todo_input')
        todo_input.send_keys('test_todo_to_be_updated')
        submit_todo_button = self.driver.find_element(by=By.ID, value='submit_todo_button')
        submit_todo_button.click()
        time.sleep(1)
        print("Editing todo")
        edit_todo_button = self.driver.find_elements(by=By.ID, value='update_todo_button')[-1]
        edit_todo_button.click()
        time.sleep(2)
        expected_state = 'Completed'
        result = self.driver.find_elements(by=By.ID, value='state')[-1]
        
        self.assertTrue(expected_state in result.text)

    @classmethod
    def tearDownClass(inst):
        inst.end = time.time()
        elapsedtime=inst.end-inst.start
        print("\n-------\nE2E test duration: ", "{:.2f}".format(elapsedtime), "seconds")
        inst.driver.quit()
        inst.app_process.terminate()
        deleteUser()
        os.remove('test_db.db')