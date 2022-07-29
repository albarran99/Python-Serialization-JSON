from typing import Any, Dict


class User:
    def __init__(self, name: str, age: int, place: str, blood_group: str) -> None:
        self.name = name
        self.age = age
        self.place = place
        self.blood_group = blood_group


def user_from_dict(s: Dict[str, Any]) -> User:
    return User(**s)


def user_to_dict(x: User) -> Dict[str, Any]:
    return vars(x)
