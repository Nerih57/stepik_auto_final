from .base_page import BasePage
from .product_page import PageObject
from .locators import BasketLocators
from .locators import ProductPageLocators


class BasketPage(PageObject):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BasketFull), \
        "Products are in the basket, but should not be"
        
    def should_be_text_about_basket_empty(self):
        basket_empty = self.browser.find_element(*BasketLocators.BasketEmpty)
        basket_empty_text = basket_empty.text
        assert "Your basket is empty" in basket_empty_text, "Basket isn't empty"
    