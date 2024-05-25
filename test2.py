# # a = [1, 2, 3, 4,7]
# a=[2,3,4,6]
# # for i in a:
# #     print(i)
#
# # for i in range(len(a)):
# #     print(a[i])
# temp=0
#
# for i in range(len(a)):
#     if a[i]%2==0:
#         temp=a[i]
#         a[i]=a[i-1]
#         a[i-1]=temp
# print(a)


# l1=[1,2,4,8]
# print(l1[1::-1])

a = "swati"
rev = ""
# for i in a[::-1]:
#     rev = rev+i
# print(rev)

# for i in range(len(a)):
#     rev=a[i]+rev
#
# print(rev)

new=""
for i in range(len(a)):
    if i%2==0:
       new = new+a[i].upper()
    else:
        new=new+a[i]
print(new)