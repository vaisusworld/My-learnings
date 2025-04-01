#read 2 list then find the intersection using set by creating it using input
x = int(input("enter the number you want"))
list =[]
for i in range(0,x):# adding the desired numbers to the list
    a = int(input())
    list.append(a)#add the numbers to the list 
b   = int(input("Enter the number u want to add in list 2"))
c = []

for r in range(0,b):
    d = int(input())
    c.append(d)

e =[]
for i in list:#check if the 2 list has any common numbers
    for i in c:
        e.append(i)
    
print(e)