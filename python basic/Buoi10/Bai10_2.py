class Person:
    """
    Person class
    """

    age = 21


Duc = Person()


def show(a):
    print(a.__class__.__name__)


show(Duc)
show(6)
show("Duc")

# Bài 02. Xem code đã có trong file btvn_02_pet.py.
#     Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
#         - Hãy tạo ra class Pet để chứa các đối tượng của class Dog, class Pet này độc lập với class Dog (hay Pet ko kế thừa từ Dog)
#         - Sau đó, tạo 4 đối tượng kiểu Dog và gán thành thuộc tính của 1 đối tượng kiểu Pet
#             name        age
#             Tom          6
#             Jerry        9
#             Butt         3
#             Wine         1
#         - Code đoạn chương trình để in ra được như sau:
#             I have 4 dogs.
#             Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
#             And they're all mammals, of course.


class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age}."

    def speak(self, sound):
        return f"{self.name} says {sound}"


class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"


class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"
