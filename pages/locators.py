from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    Register_Email = (By.CSS_SELECTOR, "#id_registration-email")
    Register_Password = (By.CSS_SELECTOR, "#id_registration-password1")
    Register_Password_Confirm = (By.CSS_SELECTOR, "#id_registration-password2")
    Register_Button = (By.CSS_SELECTOR, "div.col-sm-6.register_form button.btn.btn-lg.btn-primary")
    
    
class ProductPageLocators():
    Add_to_basket = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in")
    
class FoundPriceAndNameLocators():
    Price = (By.CSS_SELECTOR, ".col-sm-6.product_main>p.price_color")
    Price_after_payment = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in>div.alertinner>p>strong")
    Name = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    Name_after_payment = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)>div.alertinner>strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketLocators():
    BasketEmpty = (By.CSS_SELECTOR, "#content_inner")
    BasketFull = (By.CSS_SELECTOR, "div > h3")