from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def agregar_mochila(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK)).click()

    def cantidad_carrito(self):
        return self.wait.until(EC.visibility_of_element_located(self.BADGE)).text