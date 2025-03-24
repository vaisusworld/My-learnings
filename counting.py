a = str(input("Enter a string: ").lower)
b = 0 
for i in a:
    if i in "aeiou":
        b=+1
print("the number of wovel is equal to ",b)