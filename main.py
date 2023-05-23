import logging
class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self , a , b):
        suma = a + b
        self.logger.info(f"{a} + {b} = {suma}")
    def div(self , a , b):
        if a != 0 or b != 0:
            div = a / b
            self.logger.info(f"{a} / {b} = {div}")
        else:
            raise ValueError("Ділення на 0 не можливо")
    def minus(self , a , b):
        minus = a - b
        self.logger.info(f"{a} - {b} = {minus}")
    def dobutok(self , a , b):
        dobutok = a * b
        self.logger.info(f"{a} * {b} = {dobutok}")

finish = Calculator()
finish.minus(10 , 5)
finish.add(9 , 3)
finish.dobutok(5 , 4)
finish.div(10 , 0)