n = str(input("nter the sring to check"))
m = n[:1]
def pal(x,y):
    if x==y:
        return "Its is palintrom"
    else:
        return "It is not palintrom"

print(pal(n,m))