from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()          # выполняем метод страницы - переходим на страницу корзины
    page.should_not_be_products_in_basket()
    page.should_be_text_about_basket_empty()