import json
import test
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "student_id": self.student_id
        }

    def save(self):
        file = f"{self.name}_Info.json"
        with open(file, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    def display(self):
        file = f"{self.name}_Info.json"
        with open(file, "r") as f:
            info = json.load(f)
            print(json.dumps(info, indent=4))
