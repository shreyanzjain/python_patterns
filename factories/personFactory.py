from student import Student
from teacher import Teacher


class PersonFactory:

    def build_person(person_type, pname):
        if person_type == 'Student':
            return Student(name=pname)
        elif person_type == 'Teacher':
            return Teacher(name=pname)
        else:
            print('Invalid Type')
            return -1


if __name__ == '__main__':
    chcType = input('Select Type: ')
    chcName = input('Enter Name: ')
    person = PersonFactory.build_person(person_type=chcType, pname=chcName)
    person.person_method()
