from personInterface import IPerson


class Teacher(IPerson):
    def __init__(self, name):
        self.name = name

    def person_method(self):
        print(f"Hello from teacher {self.name}")
