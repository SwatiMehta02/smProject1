from operations2.play_with_numbers import is_even

# odd_count=0
# even_count=0

# for i in range(15,500):
#     if is_even(i):
#         even_count = even_count+1
#     else:
#         odd_count=odd_count+1
# print(even_count,odd_count)


for i in range(51,150):
    # if i % 87 == 0: #True
    #     print("if number is divisible by 87 stopping it")
    #     break

    if is_even(i):
        # print("Num:",i,"and cube of",i,"is",i**3)
        print(f"Num: {i} and cube of {i}, is {i**3}")
    else:
        print("Num: {0},square of num, {1} ,is {2}".format(i, i, i**2))
print("run")
# num is 5 and it is even numbers: true/false