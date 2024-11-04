from . page import Page
from selenium.webdriver.common.keys import Keys

class PickupLocationPage(Page):

    location_search_bar_selector = '//*[text()="Искать на карте"]/../textarea'
    select_location_selector = '//*[contains(text(),"Заберу отсюда")]/../..'

    def find_on_map(self, location):
        search_bar = self.get_element(self.location_search_bar_selector)
        search_bar.send_keys(location)
        self.wait(2)
        search_bar.send_keys(Keys.DOWN, Keys.RETURN)
        self.wait(3)

    def select_pikckup(self):
        self.get_element(self.select_location_selector).click()
        self.wait_load()
        self.wait(2)