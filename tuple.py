#Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result


a = int(input())
b = [int(i) for i in input().split()]
c = tuple(b)
print(c)