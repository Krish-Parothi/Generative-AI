from typing import TypedDict

class Person(TypedDict):

    name: str
    age: str

new_person : Person = {'name':"Krish", 'age':25}

print(new_person)