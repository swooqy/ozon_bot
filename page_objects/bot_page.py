from . page import Page

class BotPage(Page):
    search_bar_selector = '//*[@data-widget="searchBarDesktop"]//input'
    update_selector = '//*[@id="reload-button"]'
    
    def update_if_needed(self):
        self.wait_load()
        retry_count = 0
        while retry_count < 5:
            if self.element_exists(self.update_selector):
                self.get_element(self.update_selector).click()
            if self.element_exists(self.search_bar_selector):
                return
            else:
                self.wait_load()
                retry_count += 1
        raise Exception('Couldnt pass bot verification')

