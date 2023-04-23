from personInterface import IPerson


class Student(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"Hello from student {self.name}")
