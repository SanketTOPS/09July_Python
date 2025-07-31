data=['python','php','java','c++','go']
"""print(data)

print(data[0])
print(data[-1])
print(data[0:2]) #range
print(data[1:])
print(data[:3])
print(len(data))"""


"""for i in data:
    print(i)

print(data.index("java"))"""

"""for i in data:
    print(f"{data.index(i)} - {i}")"""

# ------------------------------------ #
#print(data)
#data[3]="c" #Update the value
#print(data)

"""if 'Python' in data:
    print("Yes...")
else:
    print("Noo")"""

# ------------------------------------ #
# List Methods

print(data)
#data.append("html")
#data.insert(2,'swift')
#data.remove('c++')
#data.pop()
#data.pop(1)
#data.clear()
#data.sort()
#data.reverse()
#del data[1]
#del data
#print(data)

"""newtdata=data.copy()
print(newtdata)"""

newdata=['html','css','scss','js']
print(newdata)

#print(data+newdata)
data.extend(newdata)
print(data)