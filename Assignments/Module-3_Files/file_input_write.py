x=open('stdata.txt','w')

id=input("Enter an ID:")
nm=input("Enter a Name:")

x.write(f"ID:{id}")
x.write(f"Name:{nm}")