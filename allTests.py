import unittest
from StandarUser import Test_Saucedemo01
from lockUser import Test_Saucedemo02
from problem_user import Test_Saucedemo03
from glitchUser import Test_Saucedemo04

if __name__ == '__main__':
    # Crea una suite de pruebas que incluya todas las clases de prueba
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Saucedemo01)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Saucedemo02))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Saucedemo03))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Saucedemo04))

    # Ejecuta la suite de pruebas
    unittest.TextTestRunner(verbosity=2).run(suite)