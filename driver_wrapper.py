from selenium import webdriver
#import undetected_chromedriver as uc

class DriverWrapper:
    driver = None

    def __init__(self, userdatadir):
        self.userdatadir = userdatadir

    def get_chrome_driver(self):
        if self.driver:
            return self.driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--user-data-dir={self.userdatadir}")
        #chrome_options.add_argument(f"--window-size=1366,768")
        #chrome_options.add_argument("--proxy-server=188.32.100.60:8080")
        self.driver = webdriver.Chrome(options=chrome_options)
        #self.driver = uc.Chrome(options=chrome_options)
        return self.driver
    
    def close_driver(self):
        if self.driver:
            self.driver.close()
            self.driver = None

