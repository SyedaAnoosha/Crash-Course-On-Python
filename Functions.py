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

def triangle_area(base, height):
    return (base*height)/2

print("Area of traingle A: "+ str(triangle_area(3,9)))
print("Area of traingle B: "+ str(triangle_area(4,8)))

# That double slash operator is called floor division. A floor division divides a number and takes the integer part of the division
# as the result. For example, five slash slash two is two instead of 2.5. 


def convert_seconds (seconds): 
    hours = seconds // 3600  
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result1 = convert_seconds(4938)
print(type(result1))
print(result1)

hours, minutes, seconds = convert_seconds(6003)
print(hours, minutes, seconds)

# some additional built-in functions:

num = 100
num1 = 44
num2= 667.745
print(abs(num))
print(pow(num1,num))
print(max(num,num1))
print(min(num,num1))

name = "Anoosha"
print(len(name) * 9)