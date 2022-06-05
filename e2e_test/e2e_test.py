import multiprocessing
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase

from app import main

DRIVER_PATH = 'chromedriver.exe'
class TestEnd2End(TestCase):
    
    @classmethod
    def setUpClass(inst) -> None:
        inst.app_process = multiprocessing.Process(target=main, args=('test_database.db',))
        inst.app_process.start()
        time.sleep(5)
        inst.start = time.time()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-gpu')
        inst.driver = webdriver.Chrome(DRIVER_PATH)
        inst.driver.get('http://localhost:5000/')
        inst.driver.save_screenshot('./e2e Test/Screenshots/01_homepage.png')

    def test_register(self):
        pass
        # self.driver.get("http://localhost:5000")
        # print("Registering")

    @classmethod
    def tearDownClass(inst):
        inst.end = time.time()
        elapsedtime=inst.end-inst.start
        print("\n-------\nE2E test duration: ", "{:.2f}".format(elapsedtime), "seconds")
        inst.driver.quit()
        inst.app4test_process.terminate()
        os.remove('test_database.db')