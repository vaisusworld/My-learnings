#Create a dictionary with 5 key-value pairs
dict = {"hi":"apple","hello":"world","name":"vaisakh","age":17,"fruits":"watermelon"}


#2
print(dict["age"])


#3
dict["cherry"] = 3

#4
dict["age"] = 16
#5
del dict["hi"]
#6
key_to_check = "watermelon"
if key_to_check in dict:
    print("yes")
else:
    print("no")
#7
for key in dict:
    print(key)

#8
new_dict = {"grape": 7, "dragon fruit": 8}
dict.update(new_dict)

#9
print(len(dict))

#10

for key in dict:
    print(key)




 