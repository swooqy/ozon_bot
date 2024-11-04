from . page import Page

class CatalogPage(Page):
    sale_checkbox_selector = '//*[text()="Распродажа 11.11"]/../../..//label'
    delivery_dates_checkbox_selector = '//span[text()="{0}"]'
    brand_filter_selector = '//*[text()="Бренд"]/../../../../..//*[text()="{0}"]'
    search_result_sort_selector = '//*[@data-widget="searchResultsSort"]/div/div[1]/div'
    search_result_sotr_dropdown_selector = '//div[@data-popper-placement="bottom-start"]//span[text()="{0}"]'
    first_item_a_selector = '(//*[@data-widget="searchResultsV2"]/div/div[1]//a)[2]'

    def select_sale(self):
        sale_checkbox = self.get_element(self.sale_checkbox_selector)
        sale_checkbox.click()
        self.wait_load()
        self.wait(3)
    
    def select_delivery_date_filter(self, deadline_filter):
        delivery_dates_checkbox = self.get_element(self.delivery_dates_checkbox_selector.format(deadline_filter))
        delivery_dates_checkbox.click()
        self.wait_load()
        self.wait(3)

    def select_brand(self, brand_name):
        brand_filter = self.get_element(self.brand_filter_selector.format(brand_name))
        brand_filter.click()
        self.wait_load()
        self.wait(3)

    def sort_by(self, sort_type):
        sort_dropdown = self.get_element(self.search_result_sort_selector)
        sort_dropdown.click()
        self.wait_load()
        self.wait(3)
        sort_dropdown_option = self.get_element(self.search_result_sotr_dropdown_selector.format(sort_type))
        sort_dropdown_option.click()
        self.wait_load()
        self.wait(3)

    def sort_by_lowest_price(self):
        self.sort_by('Дешевле')

    def open_first_item(self):
        first_item_a = self.get_element(self.first_item_a_selector)
        first_item_a.click()
        self.wait_load()
        self.wait(3)
        self.switch_to_new_tab()
        self.close_all_except_current_tab()
