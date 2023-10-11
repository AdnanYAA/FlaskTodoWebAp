n1=int(input("Enter Number:"))
n2=int(input("Enter Number:"))
choice=int(input("Enter your choice:"))
if choice==1:
    print("Addition",n1+n2)
elif choice==2:
    print("Subtraction",n1-n2)
elif choice==3:
    print("Multiplication:",n1*n2)
elif choice==4:
    print("Division:",n1/n2)
else:
    print("You made out of choice.")