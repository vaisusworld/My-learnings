employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}#given


#Initialize dictionary with default values



new= dict.fromkeys(employees,defaults)
print(new)