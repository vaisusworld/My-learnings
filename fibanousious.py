def fib(n):#creating a function
    x=0
    y=1
    print(x)
    print(y)
    for i in range(1,n-1): # adding a for loop with the range between 1 till n-2(we alr printed the first 2 numbers)
        z=x+y#adding the variable
        x=y#changing the value
        y=z#changing z value
        print(z)
fib(8)