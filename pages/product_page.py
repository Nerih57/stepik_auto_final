from .locators import ProductPageLocators
from .locators import FoundPriceAndNameLocators
from .base_page import BasePage

class PageObject(BasePage):
    def should_be_product_page(self):
        self.add_to_basket()
        self.check_price()
        self.check_name()
                
    def should_be_promo_url(self):
        assert "?promo=newYear" in self.browser.current_url, "'?promo=newYear' not in current url"
    
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.Add_to_basket)
        link.click()
        
    def check_price(self):
        price = self.browser.find_element(*FoundPriceAndNameLocators.Price)
        price_text = price.text
        price_after_payment = self.browser.find_element(*FoundPriceAndNameLocators.Price_after_payment)
        price_after_payment_text = price_after_payment.text
        assert price_text == price_after_payment_text, "'price' does not match"
        
    def check_name(self):
        name = self.browser.find_element(*FoundPriceAndNameLocators.Name)
        name_text = name.text
        name_after_payment = self.browser.find_element(*FoundPriceAndNameLocators.Name_after_payment)
        name_after_payment_text = name_after_payment.text
        assert name_text == name_after_payment_text, "'name' does not match"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
            
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear"     