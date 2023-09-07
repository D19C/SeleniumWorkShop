from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.keys import Keys
import time

# Función que realiza las acciones de prueba en una instancia de WebDriver
def realizar_acciones_de_prueba():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get('https://www.saucedemo.com')

    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    contra = driver.find_element(By.ID, "password")
    contra.send_keys("secret_sauce")

    usuario.send_keys(Keys.ENTER)

    ButtonSauceBack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    ButtonSauceBack.click()

    ButtonSauceBike = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    ButtonSauceBike.click()

    Carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    Carrito.click()

    CheckOut = driver.find_element(By.ID, "checkout")
    CheckOut.click()

    FirstName = driver.find_element(By.ID, "first-name")
    FirstName.send_keys("Diego")

    LastName = driver.find_element(By.ID, "last-name")
    LastName.send_keys("Cruz")

    Zip = driver.find_element(By.ID, "postal-code")
    Zip.send_keys("1234")

    BContinue = driver.find_element(By.ID, "continue")
    BContinue.click()

    BFinish = driver.find_element(By.ID, "finish")
    BFinish.click()

    AlertFinish = driver.find_element(By.CLASS_NAME, "complete-header")
    assert AlertFinish.text == "THANK YOU FOR YOUR ORDER", "El valor obtenido no es igual al esperado"

    driver.quit()


# Número de usuarios virtuales concurrentes
numero_de_usuarios = 2

# Crea un ThreadPoolExecutor para ejecutar múltiples instancias de WebDriver
with ThreadPoolExecutor(max_workers=numero_de_usuarios) as executor:
    for _ in range(numero_de_usuarios):
        executor.submit(realizar_acciones_de_prueba)
