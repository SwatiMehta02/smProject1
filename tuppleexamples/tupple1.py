a = (1, 2, 3, 4)
# a[2]=44 -> we cannot assign value in tuple
# length
print(len(a))
print(max(a))
print(min(a))
# index
print(a[2])
# slice
print(a[0:3:2])
# concat tuple
print(a+(7,8))
# multiplication of tuple
print(a*2)

banks = ("sbi","boi","hdfc")
banks = banks + ('axis',)
print(banks)
