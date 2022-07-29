import json

data = {
    "user": {
        "name": "Saytama (One Punch Man)",
        "age": 22,
        "place": "Japan",
        "Blood group": "0+"
    }
}

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

user = json.dumps(data)

print(user)
