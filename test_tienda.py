from login_page import LoginPage
from inventory_page import InventoryPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_agregar_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("standard_user", "secret_sauce")
    inventario = InventoryPage(driver)
    inventario.agregar_mochila()
    assert inventario.cantidad_carrito() == "2"

def test_login_bloqueado(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out" in login.obtener_error()