import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class addPost(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_blog(self):
        # Login --------------------------------------------------------------------------------------------------------
        driver = self.driver
        user = "admin"
        pwd = "password123"
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li[1]").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        # Add Customer -------------------------------------------------------------------------------------------------
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[1]/td[1]/a").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("SeleniumTest@email.org")
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("5")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("00000")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("Selenium Test")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='customer_form']/div/div/input[1]").click()
        time.sleep(1)
        driver.get("http://127.0.0.1:8000")
        time.sleep(1)
        # Modify Customer ----------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_cust_name")
        elem.clear()
        elem.send_keys("Selenium Test Edit")
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(3)
        # Delete Customer ----------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a").click()
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000")
        assert "Customer CRUD"
        # Add Service --------------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/div/a/span").click()
        elem = driver.find_element_by_xpath\
            ("//*[@id='id_cust_name']").click()
        elem = driver.find_element_by_xpath\
            ("//*[@id='id_cust_name']/option[2]").click()
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("Selenium Test")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("100")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(3)
        # Edit Service -------------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        elem = driver.find_element_by_id("id_description")
        elem.clear()
        elem.send_keys("One ginormous testing edit Lasagna.")
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(3)
        # Delete Service -----------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a").click()
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(2)
        driver.get("http://127.0.0.1:8000")
        assert "Service CRUD"
        # Add Product --------------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='id_cust_name']").click()
        elem = driver.find_element_by_xpath("//*[@id='id_cust_name']/option[2]").click()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Selenium Cake")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("A delcious testing cake made from selenium.")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("100")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("1000")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(3)
        # Edit Product -------------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
        elem = driver.find_element_by_id("id_p_description")
        elem.clear()
        elem.send_keys("This edit is to demonstrate the ability of this script to edit the product.")
        elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(3)
        # Delete Product -----------------------------------------------------------------------------------------------
        elem = driver.find_element_by_xpath\
            ("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(2)
        assert "Product CRUD"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

