m=[0,3,4,5,6,7,0]

def greater(x):
    k=0
    for i in m :
        if i>k:
            k=i
    return k
greater(m)