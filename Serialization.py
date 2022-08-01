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

number_not_repeat = [1, 2, 3, 4]
ram_command = random.sample(number_not_repeat, 1)

user_choose_character = None

user_character = None

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
    global user_choose_character

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
          '- bloquear <==> blq\n'
          '- curarte <==> heal\n'
          '- salir del programa <==> q')
    user_command = input()

    # print(user_command)

    while user_command != 'q':
        if user_command == 'hit':
            # print(desglose_number(ram_command))
            # print(desglose_number(number_not_repeat))
            enemy_dodge()
            user_command = input()

        else:
            print('comando no valido')

            user_command = input()


def enemy_dodge():
    global ram_command
    is_user_character = chose_character_user()

    if desglose_number(ram_command) == 1:
        character_3.pv = character_3.pv - is_user_character.dmg

        if character_3.pv <= 0:
            print(character_3.name + ' Ha sido derrotado' + f'(tu vida actual: {is_user_character.pv}) \n')
            quit(0)

        print('Uff!, eso dolió ahora ' + character_3.name + ' le queda de vida ' + str(
            character_3.pv) + f'(tu vida actual: {is_user_character.pv})')

        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 2:
        print('vaya! esquivo tú ataque')
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 3:
        print('Pparece que ' + character_3.name + " esta a muy distraido y recive un golpe critico")
        is_user_character.dmg = is_user_character.dmg + 2
        character_3.pv = character_3.pv - is_user_character.dmg

        if character_3.pv <= 0:
            print(character_3.name + ' Ha sido derrotado' + f'(tu vida actual: {is_user_character.pv}) \n')
            quit(0)

        print("dios mio, eso a sido un terrible golpe a " + character_3.name + " le queda de vida " + str(character_3.pv))
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()

    elif desglose_number(ram_command) == 4:
        print('tu ataque se perdio!')
        ram_command = random.sample(number_not_repeat, 1)
        # print(ram_command)
        enemy_ia()


def enemy_ia():
    global ram_command
    is_user_character = chose_character_user()

    if desglose_number(ram_command) == 1:
        print('genial!, a fallado el ataque' + f'(tu vida actual: {is_user_character.pv})')

    elif desglose_number(ram_command) == 2:
        print('Oh no! va a atacar ')

        is_user_character.pv = is_user_character.pv - character_3.dmg

        if is_user_character.pv <= 0:
            print(is_user_character.name + ' Has perdido')
            quit(0)

        print(f'(tu vida actual: {is_user_character.pv}) \n')

    elif desglose_number(ram_command) == 3:
        print('Oh no! va a atacar ')
        print('parece que sera golpe critico!')

        character_3.dmg = character_3.dmg + 2

        is_user_character.pv = is_user_character.pv - character_3.dmg

        if is_user_character.pv <= 0:
            print(is_user_character.name + ' Has perdido')
            quit(0)

        print('uf! como dolio ese golpe critico ' + f'(tu vida actual: {is_user_character.pv})')

    elif desglose_number(ram_command) == 4:
        print('parece que esta distraido')


def chose_character_user():
    global user_choose_character
    global user_character

    if user_choose_character == "saytama" or user_choose_character == "Saytama":
        user_character = character_1

    elif user_choose_character == "vezon" or user_choose_character == "Vezon":
        user_character = character_2

    elif user_choose_character == "rathalos" or user_choose_character == 'Rathalos':
        user_character = character_3

    elif user_choose_character == "zinogre" or user_choose_character == 'Zinogre':
        user_character = character_4

    elif user_choose_character == "vezok" or user_choose_character == 'Vezok':
        user_character = character_5

    return user_character


def desglose_number(num_list: list):
    global num

    for num in num_list:

        return num


mini_figth()

# with open("datafile.json" , "w") as write:
#     json.dump(data , write)

# user = json.dumps(data)
#
# print(user)
