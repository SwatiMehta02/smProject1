set1={1,2,"s"}
#add element
set1.add(1)
set1.add((5,6)) #{1,2,"s",(5,6)}
#update - add all elements of iterable as the elements of set
set1.update((5,6)) #{1,2,(5,6),5,6,"s"}

#remove element
set1.remove(1) # remove(ele) -> remove ele from set
try:
    set1.remove(7) # if element not present returns KeyError
except Exception as ex:
    print(ex)
set1.discard(2)
set1.discard((5,6))#{5,6,"s"}
set1.discard(6)#{5,"s"}



print(set1)