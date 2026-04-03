# To create a list and iterate through it, you can use the following code:
# li=[1,2,3,4,5]
# for i in li:
#     print(i) 


# to convert list to tuple
# tup=tuple(li)
# for i in tup:
#     print(i)


# to slice a tuple
# tup1=("welcome to python programming")
# print(tup1[:1])
# tup_slice=tup1[-1]
# print(tup_slice)


# to concatenate two tuples
# tuple1=(1,2,3) 
# tuple2=(4,5,6) 
# tuple3=("a","b","c")
# tuple4=tuple1+tuple2+tuple3                     
# print(tuple4)

#delete a tuple
# del tup_slice
# print(tup_slice) # this will raise an error because tup_slice has been deleted


# tup5=(1,2,3,4,5)
# a,*b,c=tup5
# print(a) # this will print 1
# print(b) # this will print [2, 3, 4]
# print(c) # this will print 5

# to reverse a tuple
# tup=(1,2,3,4,5)
# tup_reverse=tup[::-1]
# print(tup_reverse)

# tup_rev=tuple(reversed(tup))
# print(tup_rev)