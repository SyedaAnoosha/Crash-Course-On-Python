# while loop
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
attempts(7)

multiplier = 1
result = multiplier*5
while result <= 50:
  print(result)
  multiplier += 1
  result = multiplier*5
print("Done")

# for loop
# range(start, stop, step/increment)

for n in range(10):
   print(n)

for n in range(10+1):
   print(n)

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop") 


def to_celcius(x):
   return (x-32) * 5/9

for x in range(0,101,10):
   print(x,to_celcius(x))


for n in range(1,10,2):
   print(n)

for left in range(7):
   for right in range(left, 7):
      print("[" + str(left) + "|" + str(right) + "]", end=" ")
   print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
   for away_team in teams:
      if home_team != away_team:
         print(home_team + " vs " + away_team)

def greet_friends(friends):
   for friend in friends:
      print("Hi", friend)

greet_friends("Barry")
greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])



# This function will accept two integer variables: the floor number that a passenger "enter"s an elevator and the floor
# number the passenger is going to "exit". Then, the function counts up or down from the two floor numbers.
def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = ""
    if enter > exit:
        elevator_direction = "Going down: "
        while floor >= exit:
            elevator_direction += str(floor)
            if floor > exit:
                elevator_direction += " | "
            floor -= 1
    else:
        elevator_direction = "Going up: "
        while floor <= exit:
            elevator_direction += str(floor)
            if floor < exit:
                elevator_direction += " | "
            floor += 1
    return elevator_direction

print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2

for sum in range(5):
    sum += sum
    print(sum)

for x in range(10):
    for y in range(x):
        print(y)