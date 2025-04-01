n = str(input("Enter the sring to check"))  #asking for the string
m = n[:1]#reversing the order of the asked string then stroing it in diff variable
def pal(x,y): #defining a fucntion
    if x==y:# if the asked string and the reversed string are same then print "Its is palintrom" else print "It is not palintrom"
        return "Its is palintrom"
    else:
        return "It is not palintrom"

print(pal(n,m))#printing the function with calling the variables m and n

