from triangle import is_triangle

x = int(input())
y = int(input())
z = int(input())
print(x,y,z)

if is_triangle(x,y,z):
    print("It is triangle")
else:
    print("Not a triangle")
