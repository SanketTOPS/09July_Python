class studinfo:
    #private
    __stid=12
    __stnm="Sanket"
    
    def __getdata(self): #private
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def getdata(self):
        self.__getdata()

st=studinfo()
"""print(st.__stid)
print(st.__stnm)"""

#st.getdata()
st.getdata()