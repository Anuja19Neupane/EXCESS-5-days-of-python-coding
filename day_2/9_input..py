input1=int(input("Enter 1st number:\n"))
input2=int(input("Enter 2nd number:\n"))
# sum=input1+input2
# print(f"The sum is: {sum}.\n")
funct=input("Enter the operator: \n")

if funct=="+":
    print(input1+input2)

elif funct=="-":
    print(input1-input2)

elif funct=="*":
    print(input1*input2)
elif funct=="/":
    print(input1/input2)

else:
    print("invalid operator")


