aparts = [
    {
        "gym": True,
        "office": False,
        "school": False,
        "park": True,
        "supermarket": False,
        "hospital": True
    },
    {
        "gym": False,
        "office": False,
        "school": False,
        "park": False,
        "supermarket": True,
        "hospital": False
    },
    {
        "gym": True,
        "office": False,
        "school": True,
        "park": True,
        "supermarket": True,
        "hospital": False
    },
    {
        "gym": False,
        "office": False,
        "school": True,
        "park": True,
        "supermarket": False,
        "hospital": True
    },
    {
        "gym": False,
        "office": False,
        "school": False,
        "park": False,
        "supermarket": False,
        "hospital": True
    },
    {
        "gym": True,
        "office": True,
        "school": False,
        "park": False,
        "supermarket": True,
        "hospital": False
    },
    {
        "gym": False,
        "office": True,
        "school": True,
        "park": False,
        "supermarket": False,
        "hospital": True
    },
    {
        "gym": True,
        "office": False,
        "school": True,
        "park": False,
        "supermarket": True,
        "hospital": True
    },
    {
        "gym": False,
        "office": True,
        "school": False,
        "park": True,
        "supermarket": False,
        "hospital": False
    }
]
minIndex = 1e9
maxDist = 1e9
for i in range(len(aparts)):
    req = {
        "gym":1e9,
        "office":1e9,
        "school":1e9,
        "park": 1e9,
        "supermarket": 1e9,
        "hospital": 1e9
    }
    for j in range(len(aparts)):
        for k in req.keys():
            if aparts[j][k]:
                req[k] = min(req[k], abs(j-i))
    if maxDist>max(req.values()):
        maxDist = max(req.values())
        minIndex = i

print(minIndex,maxDist)

