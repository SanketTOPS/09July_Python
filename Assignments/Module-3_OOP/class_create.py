class studinfo:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is myfunc.")

#Object of class
st=studinfo()

print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()