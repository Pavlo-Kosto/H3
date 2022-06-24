# 1 Модифицировал
class Soda():
    """
    Сода с добавкой
    """

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        for k, v in globals().items():
            if v is self:
                if self.add:
                    print(f'{k} и {self.add}')
                else:
                    print("Обычная газировка")


pepsi = Soda()
pepsi.show_my_drink()
pepsi = Soda("mentos")
pepsi.show_my_drink()


# 2

class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.name != "Николай":
            print(f'я не {self.name}, я НИКОЛАЙ!!!')
            self.name = f'я не {self.name}, я НИКОЛАЙ!!!'

    __slots__ = ["name", "age"]


max = Nikola("Мах", '27')
print(max.name)


# 3

class Student:
    name = "Ivan"
    age = 18
    groupNumber = 10

    def getName(self, name):
        print(name)

    def getAge(self, ages):
        print(ages)

    def getGroupNumber(self, numbers):
        print(numbers)

    def setName(self, names):
        Student.name = names
        print(Student.name)

    def setAge(self, ages):
        Student.age = ages
        print(Student.age)

    def setGroupNumber(self, numbers):
        Student.groupNumber = numbers
        print(Student.groupNumber)


jopa = Student()
jopa.getName("Jopa")
jopa.getAge(17)
jopa.getGroupNumber(134)

Valia = Student()
Valia.getName("Valia")
Valia.getAge(18)
Valia.getGroupNumber(114)

Dimon = Student()
Dimon.getName("Dimon")
Dimon.getAge(29)
Dimon.getGroupNumber(234)

Slavik = Student()
Slavik.getName("Slavik")
Slavik.getAge(27)
Slavik.getGroupNumber(224)

Dasha = Student()
Dasha.getName("Dasha")
Dasha.getAge(23)
Dasha.getGroupNumber(204)


# 4

class Math:
    a = 26
    b = 3

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def subtraction(self, a, b):
        return a - b

# 5

class Car:
    color = "red"
    type = "sedan"
    year = 3001

    def getStart(self):
        print("авто заведен")

    def getStop(self):
        print("авто заглушен")

    def getYear(self, year):
        print(year)

    def getType(self, type):
        print(type)

    def getColor(self, color):
        print(color)
honda = Car()
honda.getStart()
honda.getType("civic")