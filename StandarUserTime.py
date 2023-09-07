from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class Test_Saucedemo01(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)
        driver = self.driver
        #driver.implicitly_wait(10)
        
    def test_StandarUser(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com')
        driver.maximize_window()

        usuario = driver.find_element(By.ID,"user-name")
        usuario.send_keys("standard_user")
        time.sleep(5)
        
        contra = driver.find_element(By.ID,"password")
        contra.send_keys("secret_sauce")
        time.sleep(5)

        usuario.send_keys(Keys.ENTER)

        ButtonSauceBack = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        ButtonSauceBack.click()
        time.sleep(5)

        ButtonSauceBike = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        ButtonSauceBike.click()
        time.sleep(5)

        Carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        Carrito.click()
        time.sleep(5)

        CheckOut = driver.find_element(By.ID,"checkout")
        CheckOut.click()
        time.sleep(5)

        FirstName = driver.find_element(By.ID,"first-name")
        FirstName.send_keys("Diego")
        time.sleep(5)

        LastName = driver.find_element(By.ID,"last-name")
        LastName.send_keys("Cruz")
        time.sleep(5)

        Zip = driver.find_element(By.ID,"postal-code")
        Zip.send_keys("1234")
        time.sleep(5)

        BContinue = driver.find_element(By.ID,"continue")
        BContinue.click()
        time.sleep(5)

        BFinish = driver.find_element(By.ID,"finish")
        BFinish.click()
        time.sleep(5)

        AlertFinish = driver.find_element(By.CLASS_NAME,"complete-header")
        assert AlertFinish.text == "Thank you for your order!", "El valor obtenido no es igual al esperado"
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()