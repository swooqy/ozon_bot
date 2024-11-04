from . page import Page

class CartPage(Page):

    go_to_payment_button_selector = '(//*[text()="Перейти к оформлению"]/../..)[1]'
    pickup_location_button_selector = '//*[text()="Самовывоз"]//../../..'
    new_pickup_location_button = '//*[@data-widget="commonAddressBook"]//button'

    def get_order_price(self):
        pass
    def go_to_payment(self):
        self.get_element(self.go_to_payment_button_selector).click()
        self.wait_load()
        self.wait(3)
    def open_pickup_selection_menu(self):
        self.get_element(self.pickup_location_button_selector).click()
        self.wait_load()
        self.wait(2)
    def add_new_pickup_point(self):
        self.get_element(self.new_pickup_location_button).click()
        self.wait_load()
        self.wait(5)
