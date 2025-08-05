def sum(a,b):
    print("Sum:",a+b)
def sub(a,b):
    print("Sub:",a-b)
def mul(a,b):
    print("Mul:",a*b)
def div(a,b):
    print("Div:",a/b)


print("1:Sum")
print("2:Sub")
print("3:Mul")
print("4:Div")
choice=int(input("Enter your choice:"))
no1=int(input("Enter Number1:"))
no2=int(input("Enter Number2:"))

if choice==1:
    sum(no1,no2)
elif choice==2:
    sub(no1,no2)
elif choice==3:
    mul(no1,no2)
elif choice==4:
    div(no1,no2)
else:
    print("Error!Invalid Choice...")