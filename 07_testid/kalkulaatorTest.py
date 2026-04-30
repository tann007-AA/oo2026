# test_calculator.py
import unittest
from kalkulaator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_initial_display(self):
        # Kontrollime, kas alguses on ekraan "0"
        self.assertEqual(self.calc.display, "0")

    def test_addition_process(self):
        # 1. Sisestame 5
        self.calc.press_number("5")
        self.assertEqual(self.calc.display, "5")
        
        # 2. Vajutame "+"
        self.calc.press_operator("+")
        # Ekraan peaks jääma samaks või tühjenema uue numbri jaoks
        # Selles loogikas ootame, et ta valmistub uueks numbriks
        
        # 3. Sisestame 3
        self.calc.press_number("3")
        
        # 4. Vajutame "="
        self.calc.press_equal()
        self.assertEqual(self.calc.display, "8")
    
    def test_division_by_zero(self):
        # 1. Sisestame 10
        self.calc.press_number("10")
        # 2. Vajutame "/"
        self.calc.press_operator("/")
        # 3. Sisestame 0
        self.calc.press_number("0")
        # 4. Vajutame "="
        self.calc.press_equal()
        
        # Ootame, et ekraanil oleks tekst "Viga", mitte et programm pange jookseks
        self.assertEqual(self.calc.display, "Viga")
        
if __name__ == '__main__':
    unittest.main()