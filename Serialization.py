import json
from User import user_to_dict, user_from_dict

data = {
    "name": "Saytama (One Punch Man)",
    "age": 22,
    "place": "Japan",
    "blood_group": "0+"
}

usr = user_from_dict(data)
print(usr.name)

usr_dict = user_to_dict(usr)
print(usr_dict["place"])

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

# user = json.dumps(data)
#
# print(user)
