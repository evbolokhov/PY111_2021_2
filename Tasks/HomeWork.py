import requests

class Money:
    def __init__(self, rub, cop):
        self.rub = rub
        self.cop = cop

    def __sub__(self, other):
        return Money(self.rub - other.rub, self.cop - other.cop)

    def subChecker(self):
        if self.cop < 0:
            self.rub -= 1
            self.cop = 100 + self.cop
            return self.rub, self.cop

    def __add__(self, other):
        return Money(self.rub + other.rub, self.cop + other.cop)

    def addChecker(self):
        if self.cop >= 100:
            self.rub += 1
            self.cop -= 100
            return self.rub, self.cop

    def __mul__(self, other):
        return Money(self.rub * other.rub, self.cop * other.cop)

    def mulChecker(self):
        while self.cop >= 100:
            self.rub += 1
            self.cop -= 100
        return self.rub, self.cop

    def __floordiv__(self, other):
        return Money(self.rub // other.factor, self.cop // other.factor)

    def __itruediv__(self, other):
        self.rub /= other.factor
        self.cop /= other.factor
        return self

    def __imul__(self, other):
        self.rub *= other.factor
        self.cop *= other.factor
        return self

    def __it__(self, other):
        return self.rub < other.rub

    def __eq__(self, other):
        return self.rub == other.rub

    # Python программа для конвертации валюты
    # из одной страны в другую

    # Импортировать необходимые модули



class Currency_convertor:

    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Извлечение только данных из данных JSON

        self.rates = data["rates"]

        # функция для простого кросс-умножения между

    # сумма и показатели конверсии

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount

        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # ограничение точности до 2 десятичных знаков

        amount = round(amount * self.rates[to_currency], 2)

        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


if __name__ == "__main__":


    def test_money():
        m1 = Money(55, 95)
        m2 = Money(50, 20)




    url = str.__add__('http://data.fixer.io/api/latest?access_key=', '43cdc6bf7bce21c5f2ce2dfbe0a76b9d')

    c = Currency_convertor(url)

    from_country = input("From Country: ")

    to_country = input("TO Country: ")

    amount = int(input("Amount: "))

    c.convert(from_country, to_country, amount)


