import pandas

data={
    "id":[1,2,3,4,5],
    "name":["sanket","nirav","ashok","darshan","gopal"],
    "city":["rajkot","baroda","bhavnagar","morbi","navsari"]
}

dt=pandas.DataFrame(data)
print(dt)

#print(data)