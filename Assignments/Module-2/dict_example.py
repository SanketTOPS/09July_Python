stdata={
    "id":101,
    "name":"sanket",
    "city":"rajkot"
}

"""print(stdata)
print(stdata["id"])
print(stdata.get("city"))
print(stdata.keys())
print(stdata.values())
print(len(stdata))
"""

# ------------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i in stdata:
    print(stdata[i])"""

for i,j in stdata.items():
    print(f"Key={i} and Value={j}")