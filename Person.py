from typing import Any, Dict


class Humans:
    def __init__(self, name: str, age: int, place: str, blood_group: str) -> None:

        self.name = name
        self.age = age
        self.place = place
        self.blood_group = blood_group


def say_hello(user):
    print('Hola mi nombre es ' + user.name)
    print('Tengo ' + str(user.age) + ' años')
    print('Soy de ' + user.place)
    print('Mi grupo sanguineo es ' + user.blood_group)


def user_from_dict(s: Dict[str, Any]) -> Humans:
    return Humans(**s)


def user_to_dict(x: Humans) -> Dict[str, Any]:
    return vars(x)
