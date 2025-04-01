#factorial number == 8*7*6*5*4*3*2*1
n =int(input("enter a number"))
m = 1

for i in range(1,n+1):
    m =i*m
print(m)

## ask for input
#let an integer be m with value as 1 stored
#for any number in range fo 1 to n  m will be changed tot m x the number(i)
#then printing the m outside for loop