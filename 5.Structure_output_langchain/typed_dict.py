from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    city: str

person_info: Person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person_info)