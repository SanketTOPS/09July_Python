"""stdata=[{"id":101,"name":"sanket"},
        {"id":102,"name":"nirav"},
        {"id":103,"name":"ashok"}]

#print(stdata)

for i in stdata:
    print(i)

for i in stdata:
    print(i["name"])"""


# --------------------------------- #
stdata={
    "st1":{"id":101,"nm":"sanket"},
    "st2":{"id":102,"nm":"nirav"},
    "st3":{"id":103,"nm":"ashok"}
}

#print(stdata)
#print(stdata["st1"])
print(stdata["st1"]["nm"])