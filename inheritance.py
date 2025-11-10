# class Car:
#     @staticmethod
#     def start():
#         print("car is started")
#     def __init__(self,name):
#         self.name = name
#
#
# class ToyotaCar(Car):
#     def Carname(self,model):
#         print("car name is", self.name)
# car1 = ToyotaCar("Mercidies")
# print(car1.name)
# ///////////////////
from tkinter.font import names


class Car:
    @staticmethod
    def start():
        print("car is started")
    def __init__(self,name):
        self.name = name


class ToyotaCar(Car):
    def super().__init__(self,model):
        self.model = model
        super().(name)

car1 = ToyotaCar("Mercidies")
print(car1.name)