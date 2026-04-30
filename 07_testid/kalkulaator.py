# calculator.py

class Calculator:
    def __init__(self):
        self.display = "0"
        self.current_value = 0
        self.operator = None
        self.new_number_started = True

    def press_number(self, number_str):
        if self.new_number_started:
            self.display = number_str
            self.new_number_started = False
        else:
            self.display += number_str

    def press_operator(self, op):
        self.current_value = int(self.display)
        self.operator = op
        self.new_number_started = True

    def press_equal(self):
        if self.operator is None:
            return
        
        second_value = float(self.display)
        result = 0
        
        if self.operator == "+":
            result = self.current_value + second_value
        elif self.operator == "-":
            result = self.current_value - second_value
        elif self.operator == "*":
            result = self.current_value * second_value
        elif self.operator == "/":
            if second_value == 0:
                self.display = "Viga"
                self.new_number_started = True
                return
            result = self.current_value / second_value
            
        self.display = format(result, '.10g')
        self.operator = None
        self.new_number_started = True 
        pass