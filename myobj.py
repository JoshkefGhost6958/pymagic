import turtle


class student:

    def __new__(cls, name, age, password, admission, * args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age, password, admission):
        self.__name = name.upper()
        self.__age = age
        self.__password = password
        self.__admission = admission
        #{"message": "init initialised the object"}

    @property  # read only property it cannot be altered
    def passwd(self):
        return {"deactivation code": 3345, "user passsword": self.__password}

    @property
    def school(self):
        _schoolName = "kyu"  # this is a prtected variable
        return {"current school": _schoolName}

    @passwd.setter
    def passd(self, value):
        self.__password = value

    @property
    def admission(self):
        return {"admission number": self.__admission}

    @admission.setter
    def admit(self, value):
        self.__admission = value

    def about(self):
        return {"output": [{"student name": self.__name, "age": self.__age}]}

    def __call__(cls, name, age):
        print("when student method is called as function:")
        return {"output:": [{"student name": name.upper(), "age": age}]}

    def __str__(self):
        return f"output:: student name {self.__name} age {self.__age}"

    def __hash__(self, password):
        self.password = password
        print(hash(password))
        return hash(password)


joe = student(name="joe", age=22, password="joshu22", admission=9999)
vic = student("vic", 22, "viceroy", 8899)
#print(joe == vic)
# if joe < vic:
#    print("joe is younger than vic")
print(joe.passwd)
print(joe.about())
print(joe.admission)
joe.admit = 11100
joe.passd = "hunterxhunter"
print(f"{joe.admission}\n{joe.passd}")
# print(joe.__dict__)
# print(joe.__dir__)
print(joe.school)


def main():
    pass


if __name__ == "__main__":
    main()
