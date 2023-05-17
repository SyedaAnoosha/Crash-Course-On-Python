#if else
def hint_username(username): 
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
       print("Valid username")

hint_username("Me") 
hint_username("Anoosha04")

def is_positive(number):
  if number > 0:
    return True
  else:
    False

print(is_positive(-40))

#elif
def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection" 
    else:
        translation = "Unknown error code"
    return translation

print(translate_error_code("404 Not Found"))


number = 25

if number <= 5: 
   print("The number is 5 or smaller.")
elif number == 33:
   print("The number is 33.")
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
else:
   print("The number is " + str(number))


# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
  whole_number = number // x # 35//10 will return 3 instead of 3.5
  remainder = number % x
  if remainder >= 5: 
    return x*(whole_number+1)
  return x*whole_number

print(round_up(35)) # Should print 40


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return filesize

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
