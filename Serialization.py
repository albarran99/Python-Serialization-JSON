import json
import random

from Person import say_hello, Humans
from Non_organic import say_hello_nonOrganic, Bionicle
from Animal import say_hello_animals, Monsters

character_1 = Humans('Saytama', 22, 'Japan', 'O+')
character_2 = Bionicle('Vezon', 16, 'Voya nui', 'teletransporte', 20, 4)
character_3 = Monsters('Rathalos', 17, 'Japan', 'llamas', 20, 4)
character_4 = Monsters('Zinogre', 12, 'Japan', 'truenos', 20, 4)
character_5 = Bionicle('Vezok', 16, 'Japan', 'ladron de poder', 20, 4)


ram_command = random.randint(1, 3)

say_hello(character_1)
print("\n")
say_hello_nonOrganic(character_2)
print("\n")
say_hello_animals(character_3)
print("\n")
say_hello_animals(character_4)
print("\n")
say_hello_nonOrganic(character_5)
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
                print(ram_command)
                enemy_dodge()
                user_command = input()

        else:
            print('comando no valido')

            user_command = input()


def enemy_dodge():
    global ram_command

    if ram_command == 1:

        character_3.pv = character_3.pv - character_2.dmg

        if character_3.pv <= 0:
            print(character_3.name + ' Ha sido derrotado' + f'(tu vida actual: {character_2.pv}) \n')
            quit(0)

        print('Uff!, eso dolió ahora ' + character_3.name + ' le queda de vida ' + str(
                character_3.pv) + f'(tu vida actual: {character_2.pv})')

        ram_command = random.randint(1, 3)
        print(ram_command)
        enemy_ia()

    elif ram_command == 2:
        print('vaya! esquivo tú ataque')
        ram_command = random.randint(1, 3)
        print(ram_command)
        enemy_ia()

    else:
        print('tu ataque se perdio!')
        ram_command = random.randint(1, 3)
        print(ram_command)
        enemy_ia()


# def ramdon_number():
#     global ram_command
#
#     print(ram_command)
#     count = [int]
#     if ram_command == 1:
#         count = count + 1
#         if count == 2:
#             ram_command = 3
#
#     elif ram_command == 2:
#         count = count + 1
#         if count == 2:
#             ram_command = 1
#
#     elif ram_command == 3:
#         count = count + 1
#         if count == 2:
#             ram_command = 2
#
#     return ram_command


# def times_to_dodge():
#     can_dodge = random.randint(0, 1)
#     count = 0
#     if can_dodge == 1:
#         count = count + 1
#         if count == 2:
#             can_dodge == 1
#
#     elif can_dodge == 0:
#         count = count + 1
#         if count == 2:
#             can_dodge == 1
#
#     return can_dodge


def enemy_ia():

    global ram_command

    if ram_command == 1:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {character_2.pv})')

    elif ram_command == 2:
        print('Oh no! va a atacar ')

        character_2.pv = character_2.pv - character_3.dmg

        if character_2.pv <= 0:
            print(character_2.name + ' Has perdido')
            quit(0)

        print(f'(tu vida actual: {character_2.pv}) \n')

    elif ram_command == 3:
        print('Oh no! va a atacar ')
        print('parece que sera golpe critico!')

        character_3.dmg = character_3.dmg + 2

        character_2.pv = character_2.pv - character_3.dmg

        if character_2.pv <= 0:
            print(character_2.name + ' Has perdido')
            quit(0)

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {character_2.pv})')

    else:
        print('parece que esta distraido')


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
