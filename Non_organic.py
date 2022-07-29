from typing import Any, Dict


class Bionicle:
    def __init__(self, name: str, human_age: int, place: str, skill: str):

        self.name = name
        self.human_age = human_age
        self.place = place
        self.skill = skill


def say_hello_nonOrganic(bionicle):
    print('Hola mi nombre es ' + bionicle.name)
    print('Tengo ' + str(bionicle.human_age) + ' años humanos')
    print('Soy de ' + bionicle.place)
    print('Mi habilidad especial es ' + bionicle.skill)
