# Tuples are sequences of elements of any type that are immutable. We write tuples in parentheses instead of square brackets.
# when using tuples the position of the elements inside the tuple have meaning
#
full_name = ('Syeda','Anoosha','Iqtidar')
first_name, middle_name,last_name = full_name
print(full_name)
print(first_name,middle_name,last_name)

def convert_seconds (seconds): 
    hours = seconds // 3600  
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result1 = convert_seconds(4938)
print(type(result1)) #<class 'tuple'>
