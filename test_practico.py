from selenium import webdriver
from selenium.webdriver.common.by import By

opciones = webdriver.ChromeOptions()
opciones.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
})
driver = webdriver.Chrome(options=opciones)
driver.implicitly_wait(10)

def ejecutar_pruebas():
    try:
        print("Ejecutando Caso 1: Login...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url
        print("✅ Caso 1 completado con éxito.")

        print("Ejecutando Caso 2: Agregar producto...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "1"
        print("✅ Caso 2 completado con éxito.")
        input("Haz la captura y presiona Enter para continuar...")

        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error
        print("✅ Caso 3 completado con éxito.")
    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas()