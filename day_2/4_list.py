grocery=["mango",100,12.3]
# if u forgot to write some data in the list we have an alternative to add the missing data
grocery.append("thisWordWasMissed")
print(grocery)
#if have to remove last data from list;
grocery.pop()
print(grocery)
print(grocery[0])# 0 index ma vako value print garxa i.e. mango
print(grocery[-1]) # last index ma vako value print garxa i.e. 12.3
length_of_list=len(grocery)
print(f"Length of list:{length_of_list}")