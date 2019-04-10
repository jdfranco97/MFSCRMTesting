import csv
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def import_list():
    with open('customers.csv', 'r') as opened_file:
        reader = csv.reader(opened_file)
        prospect_list = list(reader)
    return prospect_list


class addPost(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_blog(self):
        list = import_list()
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
        driver.get("http://127.0.0.1:8000/admin/crm/customer/")
        time.sleep(1)
        for y in range(len(list)):
            driver.find_element_by_xpath("//*[@id='content-main']/ul/li/a").click()
            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(list[y][0])
            elem = driver.find_element_by_id("id_organization")
            elem.send_keys(list[y][1])
            elem = driver.find_element_by_id("id_role")
            elem.send_keys(list[y][2])
            elem = driver.find_element_by_id("id_email")
            elem.send_keys(list[y][3])
            elem = driver.find_element_by_id("id_bldgroom")
            elem.send_keys(list[y][4])
            elem = driver.find_element_by_id("id_address")
            elem.send_keys(list[y][5])
            elem = driver.find_element_by_id("id_account_number")
            elem.send_keys(list[y][6])
            elem = driver.find_element_by_id("id_city")
            elem.send_keys(list[y][7])
            elem = driver.find_element_by_id("id_state")
            elem.send_keys(list[y][8])
            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys(list[y][9])
            elem = driver.find_element_by_id("id_phone_number")
            elem.send_keys(list[y][10])
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='customer_form']/div/div/input[1]").click()
            time.sleep(1)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()