# class Car:
#
#     def __init__(self,brand,model,year,price):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.price = price
#
#     def brand_car(self):
#         print("car name is ",self.brand)
#     def model_car(self):
#         print("model is ", self.model)
#     def year_car(self):
#         print("year is " ,self.year)
#     def price_car(self):
#         print("price is ",self.price)
#
# c1 = Car("toyota",2019,2022,90000)
# c2 = Car("suzuki",89,20,50000)
# c1.brand_car()
# print(c1.year)
#
#//////////////////////////////////////////////////
# class Average:
#     def __init__(self, name, subject1,subject2,subject3):
#         self.name = name
#         self.subject1 = subject1
#         self.subject2 = subject2
#         self.subject3 = subject3
#
#     def average_student(self):
#         avg = (self.subject1 + self.subject2 + self.subject3)/3
#         print(f"average of the {self.name}, marks is {avg}")
# a1 = Average("danyal",90,90,80)
# a1.average_student()

#   refectoring above code
#
# class Average_marks:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def avg(self):
#         sum = 0
#         for num in self.marks:
#             sum += num
#         print("hey" , self.name, "your avg marks are", (sum/3))
# a1 = Average_marks("daniyal", [90,89,78])
# a1.avg

# ///////////////////////////////////////////
class bankAccount:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

    def credit(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"you credit {amount} your new amount is {self.balance}")
        else:
            print("Recharge account")

    def dabit(self, amount):
        self.balance += amount

        print(f"you dabit {amount} your new amount is {self.balance}")

    def get_balance(self):
        print(f"current balance is {self.balance}")

danyal = bankAccount(1234, 9000)

danyal.get_balance()
danyal.credit(7000)
danyal.dabit(900)