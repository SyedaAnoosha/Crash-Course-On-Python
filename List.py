#Lists are sequences of elements of any type and are mutable

fruits = ["Pineapple", "Apple", "Mango", "Kiwi"]
print(fruits[0]) #Pinapple
print(len(fruits)) #4
print(fruits[1:3]) #['Apple', 'Mango']

print(fruits) #["Pinapple", "Apple", "Mango", "Kiwi"]
print("Orange" in fruits) #False

fruits.append("Orange")
print(fruits) #['Pineapple', 'Apple', 'Mango', 'Kiwi', 'Orange']

fruits.insert(0 ,"Banana")
print(fruits)  #['Banana', 'Pineapple', 'Apple', 'Mango', 'Kiwi', 'Orange']

fruits.remove("Apple")
print(fruits) #['Banana', 'Pineapple', 'Mango', 'Kiwi', 'Orange']

print(fruits.pop(0)) #Banana
print(fruits) #['Pineapple', 'Mango', 'Kiwi', 'Orange']

fruits[2] ="Strawberry"
print(fruits) #['Pineapple', 'Mango', 'Strawberry', 'Orange']


#enumerate function
for index, fruit in enumerate(fruits):
    print("{} - {}".format(index + 1, fruit))
# 1 - Pineapple
# 2 - Mango
# 3 - Strawberry
# 4 - Orange

print()
print("Long form code:")
multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#by list comprhension
print("List comprhension code:")
multiple = [x*7 for x in range(1,11)]
print(multiple)
print()

lengths = [len(fruit) for fruit in fruits]
print(lengths) # [9, 5, 10, 6]

three_multilpes=[ z for z in range(1,50,1) if z%3 == 0]
print(three_multilpes)  #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

print(fruits.reverse())
print(fruits.sort())
print(fruits.clear())