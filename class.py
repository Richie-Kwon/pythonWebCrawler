class User:
    def __init__(self, name) -> None:
        self.name = name 

# reference - https://www.w3schools.com/python/python_classes.asp
        
   
class Test:
    def f1():
        print("this is a class function")
    def f2(self):
        print("this is a function of instace")

class Warehouse:
    stock_num = 0
    
    def __init__(self, name) -> None:
        Warehouse.stock_num += 1
    
    def __del__ (self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Michael')
user2 = Warehouse('Alex')
user3 = Warehouse('Garry')

print (user1.__dict__)
print (user2.__dict__)
print (user3.__dict__)
print (Warehouse.__dict__)

# reference - https://www.tutorialspoint.com/What-does-built-in-class-attribute-dict-do-in-Python

# print(user1.stock_num) >> stock_num = 3
# print(user2.stock_num) >> stock_num = 3
# print(user3.stock_num) >> stock_num = 3

del user1

# print(user2.stock_num) >> stock_num = 2
# print(user3.stock_num) >> stock_num = 2