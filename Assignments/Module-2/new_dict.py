stdata={
    "id":101,
    "name":"sanket",
    "sub":"python"
}

"""print(stdata)
print(stdata["name"])
print(stdata.get("id"))
print(stdata.keys())
print(stdata.values())
print(len(stdata))"""

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

# -------------------------- #

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    print(i,j)"""

# ----------------------------- #

print(stdata)
"""stdata["city"]="rajkot" #added new pair
stdata["id"]=102
stdata.pop("sub")
stdata.clear()"""
#new=stdata.copy()
#print(new)


#del stdata["name"]
del stdata
print(stdata)