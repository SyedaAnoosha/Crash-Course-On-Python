fruit = "Mangosteen"
print(fruit[5]) #s
print(fruit[1:8]) #angoste
print(fruit[:5]) #Mango
print(fruit[5:]) #steen
print(len(fruit)) #10
print(fruit[:5] + fruit[5:]) #Mangosteen
print(fruit.index("s")) #5
print("Mango" in fruit) #True
print(fruit.lower()) #mangosteen
print(fruit.upper()) #MANGOSTEEN
print(fruit.endswith("s")) #False
print(fruit.isnumeric()) #False
print(fruit.count("e")) #2

name = "   Syeda Anoosha   "
print(name.strip()) #"Syeda Anoosha"
print(name.lstrip()) #"Syeda Anoosha   "
print(name.rstrip()) #"   Syeda Anoosha"
