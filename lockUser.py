from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class Test_Saucedemo02(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=chrome_options)
        driver = self.driver
        #driver.implicitly_wait(10)
        
    def test_LockUser(self):
        driver = self.driver
        driver.get('https://www.saucedemo.com')

        usuario = driver.find_element(By.ID,"user-name")
        usuario.send_keys("locked_out_user")
        
        contra = driver.find_element(By.ID,"password")
        contra.send_keys("secret_sauce")
        
        usuario.send_keys(Keys.ENTER)

        ButtonSauceBack = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        ButtonSauceBack.click()
        
        ButtonSauceBike = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        ButtonSauceBike.click()
        
        Carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        Carrito.click()
        
        CheckOut = driver.find_element(By.ID,"checkout")
        CheckOut.click()
        
        FirstName = driver.find_element(By.ID,"first-name")
        FirstName.send_keys("Diego")
        
        LastName = driver.find_element(By.ID,"last-name")
        LastName.send_keys("Cruz")
        
        Zip = driver.find_element(By.ID,"postal-code")
        Zip.send_keys("1234")
        
        BContinue = driver.find_element(By.ID,"continue")
        BContinue.click()

        BFinish = driver.find_element(By.ID,"finish")
        BFinish.click()

        AlertFinish = driver.find_element(By.CLASS_NAME,"complete-header")
        assert AlertFinish.text == "Thank you for your order!", "El valor obtenido no es igual al esperado"
 
    def tearDown(self):
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()