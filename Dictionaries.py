# Data in a dictionary is organized into pairs of keys and values. 
animals = { "bears":10, "lions":1, "tigers":2 , "hyenas":3, "dogs":6} 
print(animals["bears"]) #10
animals["tigers"] = 35
print("tigers" in animals) #True

del animals["lions"] #del deletes the whole key-value pair
print(animals) #{'bears': 10, 'tigers': 35, "hyenas":3, "dogs":6} 

animals.items #iteration