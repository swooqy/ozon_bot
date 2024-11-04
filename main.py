import time
from page_objects import BotPage, NavigationPage, ProductPage, CatalogPage, CartPage, PickupLocationPage
from products import ProductsDocument
from driver_wrapper import DriverWrapper

URL = 'http://www.ozon.by/'
INPUT_FILE_PATH = 'E:\\Coding\\Python\\ozon_bot\\товары.xlsx'
OUTPUT_FILE_PATH = 'E:\\Coding\\Python\\ozon_bot\\товарыицены.xlsx'
USER_DATA_PATH = 'C:/Users/knoxa/AppData/Local/Google/Chrome/User Data'
PRODUCT_INFO = {'Категория' : 'Бытовая техника',
                'Подкатегория' : 'Пылесосы',
                'Распродажа' : True,
                'Сроки доставки' : 'До 3 дней',
                'Производитель': 'Xiaomi',
                'Точка доставки' : 'Москва, Стрельбищенский переулок, 5'}


def parse_products(product_list, driver_wrapper, close=True):
    driver = driver_wrapper.get_chrome_driver()
    driver.get(URL)
    time.sleep(2) 

    bot_page = BotPage(driver)
    bot_page.update_if_needed()
    navigation_page = NavigationPage(driver)

    for product in product_list:
        navigation_page.search_article(product["ID ozon"])
        product_page = ProductPage(driver)
        if product_page.check_availability():
            product["Цена"] = product_page.get_price()
        else:
           product["Цена"] = product_page.get_price_alt()
        product["Наличие"] = product_page.get_availability()

    if close:
        driver_wrapper.close_driver()
    return product_list

def order_cheapest_product(product, driver_wrapper, close=True):
    driver = driver_wrapper.get_chrome_driver()
    driver.get(URL)
    time.sleep(2)

    navigation_page = NavigationPage(driver)
    navigation_page.go_to_category(product['Категория'], product['Подкатегория'])

    catalog = CatalogPage(driver)
    if product['Распродажа']:
        catalog.select_sale()
    catalog.select_delivery_date_filter(product['Сроки доставки'])
    catalog.select_brand(product['Производитель'])
    catalog.sort_by_lowest_price()
    catalog.open_first_item()

    product_page = ProductPage(driver)
    product_page.add_to_cart()
    navigation_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.go_to_payment()
    cart_page.open_pickup_selection_menu()
    cart_page.add_new_pickup_point()
    pickup_location_page = PickupLocationPage(driver)
    pickup_location_page.find_on_map(product['Точка доставки'])
    pickup_location_page.select_pikckup()

    if close:
        driver_wrapper.close_driver()

driver_wrapper = DriverWrapper(USER_DATA_PATH)     


#2. Открыть файл из вложения, найти товары из списка выписать цену ( без карты озона) и поставить признак есть в наличии или нет
excel_file = ProductsDocument(INPUT_FILE_PATH)
product_list = excel_file.get_products_from_file()
parse_products(product_list, driver_wrapper, False)
excel_file.write_prices_to_file(product_list, OUTPUT_FILE_PATH)

#3. Через фильтры подобрать  любые три товары одной категории, добавить их в сравнение и выбрать самый дешевый, добавив его в корзину, и выбрать доставку ( с\в с карты указать тт, где было бы удобно забрать)
order_cheapest_product(PRODUCT_INFO, driver_wrapper, False)

time.sleep(5000)


