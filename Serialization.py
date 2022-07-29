import json
import random

from Person import say_hello, Humans
from Non_organic import say_hello_nonOrganic, Bionicle
from Animal import say_hello_animals, Monsters

user1 = Humans('Saytama', 22, 'Japan', 'O+')
user2 = Bionicle('Vezon', 16, 'Voya nui', 'teletransporte', 20, 4)
user3 = Monsters('Rathalos', 17, 'Japan', 'llamas', 20, 4)
user4 = Monsters('Zinogre', 12, 'Japan', 'truenos', 20, 4)
user5 = Bionicle('Vezok', 16, 'Japan', 'ladron de poder', 20, 4)

ram_command = random.randint(1, 2)

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
          # '- bloquear <==> blq\n'
          '- salir del programa <==> q')
    user_command = input()

    # print(user_command)

    while user_command != 'q':
        if user_command == 'hit':
            if user_choose_character == 'vezon':
                print(user_choose_character + ' va a atacar a ' + user3.name + '\n')

                user3.pv = user3.pv - user2.dmg

                if user3.pv == 0:
                    print(user3.name + ' Ha sido derrotado' + f'(tu vida actual: {user2.pv}) \n')
                    quit(0)

                print('Uff!, eso dolió ahora ' + user3.name + ' le queda de vida ' + str(user3.pv) + f'(tu vida actual: {user2.pv})')

                enemy_ia()

                user_command = input()

        else:
            print('comando no valido')

            user_command = input()


def enemy_ia():
    if ram_command == 1:
        print('Oh no! va a atacar ')

        user2.pv = user2.pv - user3.dmg

        if user2.pv == 0:
            print(user2.name + ' Has perdido')
            quit(0)

        print(f'(tu vida actual: {user2.pv}) \n')

    elif ram_command == 2:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {user2.pv})')


mini_figth()

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

# user = json.dumps(data)
#
# print(user)

# elif user_command == 'blq':
#     print('Bloqueas con tus brazos. (reduccion de daño 3)' + f'(tu vida actual: {user2.pv}')
#     user3.dmg = user3.dmg - 3
#     user2.pv = user2.pv - user3.dmg
#
#     if user3.pv == 0:
#         print(user3.name + ' Ha sido derrotado' + f'(tu vida actual: {user2.pv}')
#         quit(0)
#
#     print('uff!, menos mal!!' + f'(tu vida actual: {user2.pv}')
#
#     user_command = input()
