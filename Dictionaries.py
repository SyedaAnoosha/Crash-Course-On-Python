# Data in a dictionary is organized into pairs of keys and values. 
animals = { "bears":10, "lions":1, "tigers":2 , "hyenas":3, "dogs":6} 
print(animals["bears"]) #10
animals["tigers"] = 35
print(animals.get("tigers")) #35
print("tigers" in animals) #True

print(type(animals))

del animals["lions"] #del deletes the whole key-value pair
print(animals) #{'bears': 10, 'tigers': 35, "hyenas":3, "dogs":6} 

#iteration
for key,value in animals.items():
    print("{} : {}".format(key,value))

animal1 = animals.copy()
print(animal1)
animals.clear()


def list_full_names(employee_dictionary):
    full_names = []
    for last_name, first_names in employee_dictionary.items():
        for first_name in first_names:
            full_names.append(first_name+" "+last_name)
    return(full_names)
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']
