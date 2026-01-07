# #decorator
# def add_drink(func):
#     def wrapper():
#         #returning the output of the original function, giving it a name func()
#         result = func()#refers to the function we're decorating. get_ice_cream() for example or whatever function we want to
#         #decorate.
#         print("Would you like a drink?!") #extending the original function behaviour with our decorator.
#         return result
#     return wrapper
#
# @add_drink
# def get_ice_cream():
#     print("here's your ice cream!")
#
# get_ice_cream()
#
# print()
# @add_drink
# def get_a_cookie():
#     print("here's your cookie :P!")
#
# get_a_cookie()
#class decorator

class employee():
    def __init__(self, name, salary):
        self.name = name
        self.email = name + "@comX.com"
        self.salary = salary
    def calculating_salary(self):
        multiplier = self.salary * 1.2
        final_salary = self.salary + multiplier
        return f"{self.name}'s agreed salary is {final_salary}, send him an email about it @: {self.email} "

x = employee("Ahmed", 122323)
print(x.calculating_salary())
