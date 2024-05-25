# list methods
list1 = [1, 56]
# append
list1.append("swati") #[1,56,"swati"]
list1.append([1,2,3]) #[1,56,"swati",[1,2,3]]
# insert
list1.insert(1,6) #[1,6,56,"swati",[1,2,3]]
# extend
list1.extend([16,17,[18,19]]) #[1,6,56,"swati",[1,2,3],16,17,[18,19]]
# remove
list1.remove(56) #[1,6,"swati",[1,2,3],16,17]
# count
print(list1.count(6))
# index : return index of element
# pop : removes the last element if we pass any element it will remove
# reverse : reverse the list
# sort : list1.sort(reverse:optional: True|False)
# clear : clear the list
print(list1.clear())