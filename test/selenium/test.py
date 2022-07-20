import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import environ
from selenium.webdriver.common.by import By
 
application_URL = environ.get('APPLICATION_URL', 'http://localhost:5001/')
selenium_URL = environ.get('SELENIUM_URL', 'http://192.168.44.44:4444/wd/hub')

class Test(unittest.TestCase)
    def setUp(self):
    self.driver = webdriver.Firefox()

    def test(self)
        driver = self.driver
        driver.get(application_URL)
        elem = driver.find_element(By.NAME, "name")
        elem.send_keys("Geralt")
        elem = driver.find_element(By.NAME, "animal")
        elem.send_keys("cat")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
