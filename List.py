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