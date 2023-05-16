def greeting(name):
    print("Hello", name)

greeting("Anoosha")

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Anoosha","Software Enigneering")

def add(a,b):
    sum = a+b
    return sum

result = add(100,12)
print(result)

# some additional built-in functions:

num = 100
num1 = 44
num2= 667.745
print(abs(num))
print(pow(num1,num))
print(max(num,num1))
print(min(num,num1))
print(round(num2))
