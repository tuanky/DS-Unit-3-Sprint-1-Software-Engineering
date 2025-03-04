import numpy as np 

class Product():
    """product class with default attribute: """
  
    def __init__(self, name, price=10, weight=20, flammability=0.5, 
        identifier=np.random.randint(1000000, 9999999)):
 

        self.name = name
        self.price = 10
        self.weight = 20 
        self.flammability = 0.5
        self.identifier = np.random.randint(1000000, 9999999)

        pass

    def stealability(self):
    
       x = self.price/self.weight

       if x < 0.5:
            print("Not So stealable...")
       elif (x >= 0.5 and x < 1.0):
            print("Kinda Stealable")
       else:
            print("Very stealable!") 

    def explode(self):
        
        y = self.flammability * self.weight
        
        if y < 10: 
            print("...fizzle")
        elif (y >= 10  and y < 50):
             print("...boom!")
        else:
             print("...BABOOM!!")

class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5, 
        identifier=np.random.randint(1000000, 9999999)):
 

        self.name = name
        self.price = 10
        self.weight = 10
        self.flammability = 0.5
        self.identifier = np.random.randint(1000000, 9999999)

        pass

    def explode(self):
        print("...it's a glove")

    def punch(self):
        z = self.weight
        if z < 5: 
            print("That tickles")
        elif (z >= 5  and z < 15):
             print("Hey that hurt!")
        else:
             print("OUCH!")