from . page import Page

class ProductPage(Page):
    full_price_selector = '//*[text()="без Ozon Карты"]/../../div[1]/span[1]'
    price_selector = '//*[@data-widget="webPrice"]//span'
    price_selector_alt = '//div[@data-widget="webOutOfStock"]//span[1]'
    add_to_cart_selector = '(//div[@data-widget="webAddToCart"])[1]//button'
    reason_selector = '//div[@data-widget="webOutOfStock"]/h2'
    currency_selector = '//*[@data-widget="selectedCurrency"]/div'
    
    def __init__ (self, driver):
        super().__init__(driver)
        self.get_currency()

    def get_currency(self):
        self.currency = self.get_element(self.currency_selector).text.strip()

    def check_availability(self):
        return self.element_exists(self.price_selector)
    
    def get_availability(self):
        if not self.check_availability():
            try:
                el = self.get_element(self.reason_selector)
                return el.text.strip()
            except:
                return "Невозможно узнать"
        else:
            return "Товар в наличии"

    def get_price(self):
        if self.element_exists(self.full_price_selector):
            price_el = self.get_element(self.full_price_selector)
        else:
            price_el = self.get_element(self.price_selector)
        price = "".join(filter(str.isdecimal,price_el.text))
        return self.format_price(price)
    
    def get_price_alt(self):
        if self.element_exists(self.price_selector_alt):
            price_el = self.get_element(self.price_selector_alt)
            price = "".join(filter(str.isdecimal,price_el.text))
            return self.format_price(price)
        else:
            return "Невозможно узнать"
        
    def format_price(self, price):
        if self.currency == "BYN":
            price = price[:-2] + "," + price[-2:]
        return price + " " + self.currency
    
    def add_to_cart(self):
        add_to_cart_button = self.get_element(self.add_to_cart_selector)
        add_to_cart_button.click()