class Fruit:
    flavor = ""
    color = ""

    # def __init__(self):
    #     pass

    def __init__ (self, color, flavor): # constructor
        self.flavor = flavor
        self.color = color

    def __str__(self): #conversion to string.
        return("This fruit is {} and its flavor is {}".format(self.color,self.flavor))
        

mango = Fruit("Yellow","Sweet")

print(mango.color)
print(mango.flavor)
print(mango)
help(mango)
