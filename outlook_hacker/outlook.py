import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ecd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class OutlookHacker:
    # setting option to make selenium headless
    options = Options()
    options.add_argument("--headless")

    # driver path
    path_to_driver = '../drivers/geckodriver_linux/geckodriver'
    driver = webdriver.Firefox(executable_path=path_to_driver)
    wait = None
    outlook_sign_in_url = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1588766030&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7c2e3aad-7b3d-0980-daf9-9c4ce806851a&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"
    timer = 10

    def __init__(self, email_id, password):
        self.email = email_id
        self.password = password

    # same request handler
    def element_action(self, **kwargs):
        # if element is of type input or element need just to be located
        if 'FIND' == kwargs['action']:
            if kwargs.get('input_data', None):
                ele_for_input = self.wait.until(ecd.presence_of_element_located((By.XPATH, kwargs['dom_x_path'])))
                ele_for_input.send_keys(kwargs.get('input_data'))
                return ele_for_input
            else:
                ele_for_input = self.wait.until(ecd.presence_of_element_located((By.XPATH, kwargs['dom_x_path'])))
                return ele_for_input
        # if element is a button
        elif 'CLICK' == kwargs['action']:
            btn_ele = self.wait.until(ecd.element_to_be_clickable((By.XPATH, kwargs['dom_x_path'])))
            btn_ele.click()
            return btn_ele
        return None

    # start by visiting main url
    def start(self):
        self.driver.get(self.outlook_sign_in_url)
        self.wait = WebDriverWait(self.driver, timeout=self.timer)
        return self.login()

    # enter details and login
    def login(self):
        # ele_for_input_email
        self.element_action(action='FIND', dom_x_path="//*[@id='i0116']", input_data=self.email)
        # next_btn
        self.element_action(action='CLICK', dom_x_path="//*[@id='idSIButton9']")
        # ele_for_pass
        self.element_action(action='FIND', dom_x_path="//*[@id='i0118']", input_data=self.password)
        # btn_of_sign_in
        self.element_action(action='CLICK', dom_x_path="//*[@id='idSIButton9']")
        return self.driver.get_cookies()


if __name__ == "__main__":
    d = OutlookHacker(email_id="xyz@hotmail.com", password="xklklklk")
    d.start()