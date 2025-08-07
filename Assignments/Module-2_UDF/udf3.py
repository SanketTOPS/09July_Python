def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

#getdata(101,'Sanket','Python')

n=int(input("Enter number of stud.:"))

for i in range(n):
    stid=input("Enter an ID:")
    stnm=input("Enter a Name:")
    stct=input("Enter a City:")
    getdata(stid,stnm,stct)
