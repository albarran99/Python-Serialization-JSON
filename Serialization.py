import json
from Person import say_hello, Humans
from Non_organic import say_hello_nonOrganic, Bionicle
from Animal import say_hello_animals, Monsters

user1 = Humans('Saytama', 22, 'Japan', 'O+')
user2 = Bionicle('Vezon', 16, 'Voya nui', 'teletransporte', 20, 4)
user3 = Monsters('Rathalos', 17, 'Japan', 'llamas', 20, 4)
user4 = Monsters('Zinogre', 12, 'Japan', 'truenos', 20, 4)
user5 = Bionicle('Vezok', 16, 'Japan', 'ladron de poder', 20, 4)

say_hello(user1)
print("\n")
say_hello_nonOrganic(user2)
print("\n")
say_hello_animals(user3)
print("\n")
say_hello_animals(user4)
print("\n")
say_hello_nonOrganic(user5)
print("\n")


def mini_figth():

    print('elige un personaje: \n'
          '1.''no disponible''\'\n'
          '2.vezon\n'
          '3.rathalos\n'
          '4.zinogre\n'
          '5.vezok')

    user_choose_character = input()

    print('has elejido a ' + user_choose_character)

    print('por favor escriba un comando valido:\n'
          '- atacar <==> hit\n'
          '- ver vida <==> live\n'
          '- salir del programa <==> q')
    user_command = input()

    # print(user_command)

    while user_command != 'q':
        if user_command == 'hit':
            if user_choose_character == 'vezon':
                print(user_choose_character + ' va a atacar a ' + user3.name)

                user3.pv = user3.pv - user2.dmg

                if user3.pv == 0:
                    print(user3.name + ' Ha sido derrotado')
                    quit(0)

                print('Uff!, eso dolió ahora ' + user3.name + ' le queda de vida ' + str(user3.pv))

                user_command = input()

        elif user_command == 'live':
            print('Vezon tiene ' + str(user2.pv))

            user_command = input()

        else:
            print('comando no valido')

            user_command = input()


mini_figth()

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

# user = json.dumps(data)
#
# print(user)
