from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from contextlib import contextmanager
import time

class Page:
    driver = None
    def __init__(self, driver : webdriver):
        self.driver = driver
        self.wait_load()
    def get_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    def get_elements(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)
    def element_exists(self,xpath):
        return bool(self.get_elements(xpath))
    def wait(self, sec):
        time.sleep(sec)
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    def close_all_except_current_tab(self):
        all_tab_list = self.driver.window_handles
        current_tab = self.driver.current_window_handle
        for window in all_tab_list:
            if window != current_tab:
                self.driver.switch_to.window(window)
                self.driver.close()
        self.driver.switch_to.window(current_tab)
    @contextmanager
    def wait_load(self, timeout = 20):
        old_page = self.find_element_by_tag_name('html')
        yield
        WebDriverWait(self, timeout).until(staleness_of(old_page))