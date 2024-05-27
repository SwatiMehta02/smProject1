from createpattern import draw_pattern

n=input("num:")
try:
    draw_pattern(int(n))
except ValueError as error:
    print("invalid data type")