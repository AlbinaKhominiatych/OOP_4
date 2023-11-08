#практика
class Calculator:
    #сценарій 2
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2
    #сценарій 1
    @classmethod
    def add_numbers_rounded(cls, num1, num2):
        rounded_num1 = round(num1)
        rounded_num2 = round(num2)
        return cls.add_numbers(rounded_num1, rounded_num2)

print(Calculator.add_numbers(2.7, 3.4))
print(Calculator.add_numbers_rounded(2.7, 3.4))
