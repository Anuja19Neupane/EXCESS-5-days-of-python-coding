def concatenate_string(str1,str2):
    # concatenates two string and return the result
    return str1+" "+str2
result=concatenate_string("hello","world")
print(f"The result is {result}.")





def sum_list(numbers):
    #sum up all the numbers in a list
    total=0
    for num in numbers:
        total+=num
    return total
list=[1,23,4,5,6]
result=sum_list(list)
print(result)




def remove_duplicates(lst):
    unique_list=[]
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list=[1,2,2,3,4,4,4,4,5]
result=remove_duplicates(my_list)
print(result)
