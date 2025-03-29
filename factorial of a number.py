n = int(input("Enter the number"))# asking for the number
m = 1 

def fac(x,y):# defining a fact
    for i in range(1,x+1): #from range from 0 till i 
        y = i*y #change y value until the range then muultiply 
    print(y)

print(fac(n,m))