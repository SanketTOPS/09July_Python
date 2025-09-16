class master:
    def header(self,home,about,contact):
        print("HOME:",home)
        print("ABOUT:",about)
        print("CONTACT:",contact)
    
    
class index(master):
    def header(self, home, about, contact):
        return super().header(home, about, contact)

class profile(master):
    def header(self, home, about, contact):
        return super().header(home, about, contact)
        

ind=index()
ind.header("H","A","C")

pro=profile()
pro.header("H","A","C")