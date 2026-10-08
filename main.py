#Multiple Inheritance
class Animal:
    def __init__(self,c,e):
        self.color = c
        self.eat = e

    def Show_info(self):
        print(f"Color: {self.color} ")
        print(f"Eat: {self.eat}")    

class Pet:
    def __init__(self,o):
        self.owner = o

    def Show_info(self):
        print(f"Owner : {self.owner}")

class Dog(Pet,Animal):
    def __init__(self, n,c,e,o):
        Animal.__init__(self,c,e)
        Pet.__init__(self,o)
        self.name = n

    def Show_info(self):
        print(f"Dog name:  {self.name}")
        Animal.Show_info(self)
        Pet.Show_info(self)
        
        
dog1 = Dog("tommy",'Black','meat','momo')
dog2 = Dog("tom",'Black','meat','momo')
dog3 = Dog("meow",'Black','meat','momo')

