from classes.human import MathClass, MehtaFamily

#
# m1=MathClass()
# print(m1.x)
# print(m1.addition())


s = MehtaFamily("Swati", 24)
print(s.get_father_name())
print(s.name)

h = MehtaFamily("Harsh", 23)
print(h.get_father_name())
print(h.name)

s1 = MehtaFamily("dfghj", 22)
print(s1.set_profession("asd"))
print(s1.profession)
