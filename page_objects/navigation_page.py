from .page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class NavigationPage(Page):
    search_bar_selector = '//*[@data-widget="searchBarDesktop"]//input'
    catalog_menu_selector = '//*[@data-widget="catalogMenu"]/button'
    catalog_list_selector = '(//*[@style-insert="[object Object]"]/div[1]//ul)[2]//span[text()="{0}"]'
    sub_catalog_list_selector = ('//*[@trackinginfo="[object Object]"]//a[text()="{0}"]')
    cart_menu_selector = ('//a[@href="/cart"]')

    def search_article(self, article):
        search_bar = self.get_element(self.search_bar_selector)
        search_bar.send_keys(Keys.CONTROL + "a")
        search_bar.send_keys(Keys.DELETE)
        search_bar.send_keys(article)
        search_bar.submit()
        self.wait_load()

    def open_catalog(self):
        catalog_button = self.get_element(self.catalog_menu_selector)
        catalog_button.click()
        self.wait_load()
    
    def hover_category(self, category_name):
        category_list_item_element = self.get_element(self.catalog_list_selector.format(category_name))
        ActionChains(self.driver).move_to_element(category_list_item_element).perform()
        self.wait_load()

    def select_sub_category(self, sub_category_name):
        sub_category_list_item_element = self.get_element(self.sub_catalog_list_selector.format(sub_category_name))
        sub_category_list_item_element.click()
        self.wait_load()
        self.wait(3)

    def go_to_category(self, category_name, sub_category_name):
        self.open_catalog()
        self.hover_category(category_name)
        self.select_sub_category(sub_category_name)
        self.switch_to_new_tab()
        self.close_all_except_current_tab()
        self.wait(3)

    def go_to_cart(self):
        cart_menu = self.get_element(self.cart_menu_selector)
        cart_menu.click()
        self.wait_load()
        