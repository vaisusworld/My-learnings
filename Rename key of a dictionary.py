sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
} #given

sample_dict['hi'] = sample_dict.pop('city')
print(sample_dict)