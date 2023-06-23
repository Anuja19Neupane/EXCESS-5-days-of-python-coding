a=10 # this is equivalent to int a=10; in c
b="hello"
print(a)
print(b)
print(type(a))
print(type(b))

a="10"
b=3
# print(a+b)
# note: a is string and b is int thus they can't be added
a=int(a) # this will convert a to int. so now this works
print(a+b)