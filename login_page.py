from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com"
    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def login(self, usuario, clave):
        self.wait.until(EC.visibility_of_element_located(self.USER)).send_keys(usuario)
        self.driver.find_element(*self.PASS).send_keys(clave)
        self.wait.until(EC.element_to_be_clickable(self.BTN)).click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR)).text