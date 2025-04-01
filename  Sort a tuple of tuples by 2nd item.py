tuple1 = (('a', 23),('b', 37),('d', 11), ('c',29)) #given
# Sort a tuple of tuples by 2nd item


sorted_tuple = sorted(tuple1, key=lambda x: x[0])

print(sorted_tuple)



