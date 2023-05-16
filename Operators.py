# ==    (equality)  
# !=     (not equal to)  
# >       (greater than)
# <      (less than)
# >=    (greater than or equal to)
# <=    (less than or equal to)

# Comparison Operators with Numbers
print(32 == 30+2) # True
print(9/3 != 3*1) # False

# Comparison Operators with Strings
print("a string" == "a string") #True

print("4 + 5" == 4 + 5) #False

event_city = "Hyd"
print(event_city != "Hyd") #False


# The greater than > operator checks if the left string has a higher Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can  easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. 
print("Wednesday" > "Friday") #True
 
# B has a Unicode value of 66 and b has a Unicode value of 98. This comparison is the same as 66 < 98, which is true.
print("Brown" < "brown") #True

print("sunbathe" > "suntan") #False because 'b' does not have a higher Unicode value than 't'.
# Python will check the comaprisoan in a cycle through each letter of each string.

# If two identical strings are compared using the less than < comparison operator, this will produce a False result because they are equal.
print("Lima" < "Lima") #False beacuse both the strings are same

#print("Five" < 6) #TypeError: '<' not supported between instances of 'str' and 'int'


# Logical Operators
print((6*3 >= 18) and (9+9 <= 36/2)) # True
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi") #False


x = 2*3 > 6
print("The value of x is:")
print(x)

print("The inverse value of x is:")
print(not x)

print("A">"B" or "B"<"F") #True
print(16 <= 4**2 or 9**(0.5) != 3) #True

print(not 42 == "Answer") #True