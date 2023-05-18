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

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames using as many lines of code as your chosen method requires.
newfilenames = [filename[:-3]+"h" if filename.endswith("hpp") else filename for filename in filenames ]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
  members = ", ".join(users)
  return group + ": " + members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    num = arrivals.index(name)
    return (len(arrivals) // 2 < num and (num != len(arrivals)-1))
      

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

print(fashionably_late(party_attendees,"Ford"))