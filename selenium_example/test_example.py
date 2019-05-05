from webdriver import *
import time

class TestAmazonExample(WebDriverBase):
    HOME_CATEGORY_LOCATOR = (By.CSS_SELECTOR, "#desktop-top .as-title-block-left")
    GIRISAYFA_BUTTON_LOCATOR = (By.ID, "nav-link-accountList")
    KADI_LOCATOR = (By.ID, "ap_email")
    PASS_LOCATOR = (By.ID, "ap_password")
    GIRIS_BUTTON_LOCATOR = (By.CLASS_NAME, "a-button-input")
    SEARCH_BOX_LOCATOR = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.CLASS_NAME, "nav-search-submit")
    UCUNCU_URUN_LOCATOR = (By.CSS_SELECTOR, ".s-result-list > [data-index = '1'] a")
    WISH_LIST_LOCATOR = (By.ID, "add-to-wishlist-button-submit")
    WISH_LOCATOR = (By.CSS_SELECTOR, "[id = 'WLHUC_viewlist']")
    DELETE_LOCATOR = (By.CSS_SELECTOR, "[name = 'submit.deleteItem']")

    def __init__(self):
        super().__init__()
        self.init_driver()
        self.driver.get("https://www.amazon.com")
        self.test_category()
        self.get_element(self.GIRISAYFA_BUTTON_LOCATOR).click()
        self.giris()
        self.arama("samsung")
        self.get_element(self.UCUNCU_URUN_LOCATOR).click()
        self.get_element(self.WISH_LIST_LOCATOR).click() 
        time.sleep(5)
        self.get_element(self.WISH_LOCATOR).click()
        self.get_element(self.DELETE_LOCATOR).click()
        time.sleep(1000000)

        #self.driver.quit()

    def test_category(self):
        first_category = self.get_element(self.HOME_CATEGORY_LOCATOR)
        assert first_category.text == "Discover Amazon"

    def giris(self):
        kadi = self.get_element(self.KADI_LOCATOR)
        password = self.get_element(self.PASS_LOCATOR)
        kadi.send_keys("email")
        password.send_keys("password")
        self.get_element(self.GIRIS_BUTTON_LOCATOR).click()

    def arama(self,product_name):
        search_box = self.get_element(self.SEARCH_BOX_LOCATOR)
        search_box.send_keys(product_name)
        self.get_element(self.SEARCH_BUTTON_LOCATOR).click()

    

if __name__ == '__main__':
    TestAmazonExample()
    print("TEST OK")