s1=int(input("Enter Subject1 mark:"))
s2=int(input("Enter Subject2 mark:"))
s3=int(input("Enter Subject3 mark:"))
s4=int(input("Enter Subject4 mark:"))

if s1>=40 and s2>=40 and s3>=40 and s4>=40:
    
    total=s1+s2+s3+s4
    print("Total:",total)

    pr=total/4
    print("PR:",pr)

    if pr>=70: #child
        print("Result:Dist.")
    elif pr>=60: #child
        print("Result:First Class")
    elif pr>=50: #child
        print("Result:Second Class")
    elif pr>=40: #child
        print("Result:Pass Class")
else:
    print("Result:FAIL")