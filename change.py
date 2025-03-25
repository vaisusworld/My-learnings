n = str(input("Enter your string"))

def check(x):
    if x ==x.lower():
        print(x.upper())
    elif x==x.upper():
        print(x.lower())
print(check(n))