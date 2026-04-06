import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
# to add an element to the array, we can use the append() method
a.append(6) 
for i in a:
    print(i)
# to remove an element from the array, we can use the remove() method
a.remove(3)
for i in a:
    print(i)

count=a.count(5)
print(count)