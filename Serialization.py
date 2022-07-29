import json
from Person import say_hello, Humans
from Non_organic import say_hello_nonOrganic, Bionicle
from Animal import say_hello_animals, Monsters

user1 = Humans('Saytama', 22, 'Japan', 'O+')
user2 = Bionicle('Vezon', 16, 'Voya nui', 'teletransporte')
user3 = Monsters('Rathalos', 17, 'Japan', 'llamas')
user4 = Monsters('Zinogre', 12, 'Japan', 'truenos')
user5 = Bionicle('Vezok', 16, 'Japan', 'ladron de poder')

say_hello(user1)
print("\n")
say_hello_nonOrganic(user2)
print("\n")
say_hello_animals(user3)
print("\n")
say_hello_animals(user4)
print("\n")
say_hello_nonOrganic(user5)

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

# user = json.dumps(data)
#
# print(user)
