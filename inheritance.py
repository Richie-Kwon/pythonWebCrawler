# super class 
# sub class 

class Car:
    """ parenet class"""
    def __init__(self, type, color) -> None:
        self.type = type
        self.color = color
    def show (self):
        return print ("car clsss")


class Hcar(Car):
    def __init__(self, type, color, model) -> None:
        super().__init__(type, color)
        self.model = model

    def show_H (self):
        return print ("Model : %s", self.model)

# Method overrding
    def show (self):
        return print ("method overring") 

# Inheritance info - in python
print (Hcar.mro())




