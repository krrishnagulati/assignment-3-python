# question4
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3= int(input("enter third number:"))
# num1 ,num2 , num3  are variables declared 
# using input function num1,num2,num3 are given input value

if(num1>num2):
    if(num1>num3):
        print("num1 is greatest:",num1)
    else:
        print("num3 is greatest:",num3)
if(num2>num3):
    print("num2 is greatest:",num2)
else:
    print("num3 is greatest:",num3)

   
