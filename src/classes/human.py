class Human:
    name = 'Swati'


class MathClass:
    x = 9
    y = 1

    def addition(self):
        return self.x + self.y


class MehtaFamily:
    mother = "Bindu"
    father = "Nand"
    profession = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_profession(self, profession):
        self.profession = profession

    def get_mother_name(self):
        return self.mother

    def get_father_name(self):
        return self.father
