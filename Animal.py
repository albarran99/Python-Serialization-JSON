

class Monsters:
    def __init__(self, name: str, human_age: int, place: str, elemental_attack: str):

        self.name = name
        self.human_age = human_age
        self.place = place
        self.elemental_attack = elemental_attack


def say_hello_animals(monster):
    print('Hola mi nombre es ' + monster.name)
    print('Tengo ' + str(monster.human_age) + ' años humanos')
    print('Soy de ' + monster.place)
    print('Mi ataque elemental es ' + monster.elemental_attack)
