from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage

def test_ejecucion_pom():
    driver = webdriver.Chrome()
    try:
        login = LoginPage(driver)
        login.abrir()
        login.login("standard_user", "secret_sauce")
        assert "inventory.html" in driver.current_url

        inventario = InventoryPage(driver)
        inventario.agregar_mochila()
        assert inventario.cantidad_carrito() == "1"
        print("✅ POM funcionando")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_ejecucion_pom()