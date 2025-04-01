n = str(input("Enter your string"))

def check(x):
    if x ==x.lower():
        print(x.upper())
    elif x==x.upper():
        print(x.lower())
print(check(n))

# for changing the case of a string
# fist ask for the number , using function check if the number is lower if it lower change it to uppercase and do vice versa 
#the call the  function