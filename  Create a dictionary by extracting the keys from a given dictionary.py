sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
#given

for k in keys:
    n ={k: sample_dict[k]}
        
print(n)