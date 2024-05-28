def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    return False


def is_equilateral(side1, side2, side3):
    if is_triangle(side1, side2, side3) is True:
        if side1 == side2 and side2 == side3 and side1 == side3:
            return True
    return False


def is_isosceles(num1, num2, num3):
    if is_triangle(num1, num2, num3):
        # if num1==num2 or num2==num3 or num3==num1:
        if (num1 == num2 and num2 != num3) or (num2 == num3 and num3 != num1) or (num3 == num1 and num1 != num2):
            return True
    return False


def max_of_three(a, b, c):
    max = 0  # maximum value among a,b,c
    # checking greater between a,b
    if a >= b:
        max = a
    else:
        max = b
    if max <= c:
        max = c
    # max = a if a>=b and a>=c else b if b>=c and b >=a else c
    return max

# print(max_of_three(2,3,5))

def is_right_angle_triangle(l1, l2, l3):
    if is_triangle(l1, l2, l3):
        if (l1**2==l2**2+l3**2) or (l2**2==l3**2+l1**2) or (l3**2==l1**2+l2**2):
            return True
    return False


# print(is_triangle(1,1,2))
# print(is_equilateral(1,1,1))
# print(is_isosceles(1, 3, 2))
# print(is_right_angle_triangle(11,13,5))