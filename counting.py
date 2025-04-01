a = str(input("Enter a string: ").lower)
b = 0 
for i in a:
    if i in "aeiou":
        b=+1
print("the number of wovel is equal to ",b)
#for checking if the string has vowels
#ask for the string,let a variable be 0  now let  i variable be the the string if there is any vowel letters then add tht to b then later print b
