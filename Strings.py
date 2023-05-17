#Strings are sequences of characters and are immutable. 
#String Functions 

fruit = "Mangosteen"
print(fruit[5]) #s
print(fruit[1:8]) #angoste
print(fruit[:5]) #Mango
print(fruit[5:]) #steen
print(len(fruit)) #10
print(fruit[:5] + fruit[5:]) #Mangosteen
print(fruit.index("s")) #5
print( "Mango" in fruit) #True
print(fruit.lower()) #mangosteen
print(fruit.upper()) #MANGOSTEEN
print(fruit.endswith("s")) #False
print(fruit.isnumeric()) #False
print(fruit.isalpha()) #True
print(fruit.count("e")) #2
print(fruit.split()) #['Mangosteen']
print("Mangosteen has a sweet-and-sour flavor".split()) #['Mangosteen', 'has', 'a', 'sweet-and-sour', 'flavor']
print(fruit.replace("steen","")) #Mango
print(" ".join(["Mangosteen","has","a","sweet-and-sour","flavor"])) #Mangosteen has a sweet-and-sour flavor
print("...".join(["Mangosteen","has","a","sweet-and-sour","flavor"])) #Mangosteen...has...a...sweet-and-sour...flavor
name = "   Syeda Anoosha   "
print(name.strip()) #"Syeda Anoosha"
print(name.lstrip()) #"Syeda Anoosha   "
print(name.rstrip()) #"   Syeda Anoosha"

# {} placeholder and format() examples below:
# > - align text to right
# < - align text to left

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.987)) #For only 49.99 dollars!

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

name1="Syeda Anoosha"
roll_no = "21sw004"
print(("Hello I am {}. My roll number is {}.").format(name1,roll_no))

example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)
print(formatted_string) #this is an example of using the format() method on a string
# >-
#If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).
first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string) #apple carrot banana


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
print(replace_domain("anushazaidi06@gmail.com","gmail.com","hotmail.com"))

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(sentence) - len(old)
        new_sentence = sentence[:i]  + new
        return new_sentence
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore" as "seashells" is not end of string
