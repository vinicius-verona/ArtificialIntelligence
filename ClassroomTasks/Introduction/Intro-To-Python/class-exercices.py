from tokenize import Number


class Person:
    """
    ### Classe Pessoa
    """

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return 'Person({})\n'.format(self.name)

    def __str__(self) -> str:
        return self.name


class SimpleCalculator:
    """
    ### Classe Calculadora Simples
    """

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return 'SimpleCalculator(a: {}, b: {})\n'.format(self.a, self.b)

    def __str__(self) -> str:
        return 'Calculadora Simples - a: {}, b: {}'.format(self.a, self.b)

    def add(self) -> Number:
        return self.a + self.b

    def subtract(self) -> Number:
        return self.a - self.b

    def multiply(self) -> Number:
        return self.a * self.b

    def divide(self) -> Number:
        return self.a / self.b


class Calculator:
    """
    ### Classe Calculadora
    """

    def __repr__(self) -> str:
        return 'Calculator()\n'

    def add(self, a, b) -> Number:
        return a + b

    def subtract(self, a, b) -> Number:
        return a - b

    def multiply(self, a, b) -> Number:
        return a * b

    def divide(self, a, b) -> Number:
        return a / b


class Order:
    """
    ### Classe de pedidos
    """
    _sequence = 0  # Class attribute
    _objects = []

    def __init__(self, name, description) -> None:
        self.id = None
        self.name = name  # Instance attribute
        self.description = description

    def __repr__(self) -> str:
        return 'Order(id: {}, name: {}, description: {})'.format(self.id, self.name, self.description)

    def __str__(self) -> str:
        return 'Order {} by {} = {}'.format(self.id, self.name, self.description)

    def save(self) -> None:
        self.__class__._sequence += 1
        self.id = self.__class__._sequence
        self.__class__._objects.append(self)

    @classmethod
    def all(cls):
        return cls._objects


# Testing:
print(Person("Verona"))
print(repr(Person("Verona")))

print(SimpleCalculator(1, 2))
print("add: ", SimpleCalculator(1, 2).add())
print("subtract: ", SimpleCalculator(1, 2).subtract())
print("multiply: ", SimpleCalculator(1, 2).multiply())
print("divide: ", SimpleCalculator(1, 2).divide())
print(repr(SimpleCalculator(1, 2)))

print("add(1, 2): ", Calculator().add(1, 2))
print("subtract(1, 2): ", Calculator().subtract(1, 2))
print("multiply(1, 2): ", Calculator().multiply(1, 2))
print("divide(1, 2): ", Calculator().divide(1, 2))
print(repr(Calculator()))

obj1 = Order("Verona", "x-tudo")
obj1.save()
obj2 = Order("Verona", "podrão")
obj2.save()

print(obj1)
print(obj2)
print(Order.all())
print(repr(obj2))
