# question6
side1 = int(input("enter the length of first side:"))
side2 = int(input("enter the length of second side:"))
side3 = int(input("enter the length of third side:"))
# side1,side2,side3 are variables declared for side of traingles

if(side1>+side2+side3) or (side2>=side1+side3) or (side3>=side2+side1):
    print("No")
else:
    print("Yes")
