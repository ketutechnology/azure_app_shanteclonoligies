#Write a program to perform various various operations on tuples such as adding tuples, replacing tuples, slicing tuples and deleting tuples.

tuple1=(1,2,3,4,5,6)
tuple2=("z","c","d")
add=tuple1+tuple2
print("Add Tuple : ",add)
print("The original tuple is : " + str(tuple1))
lst = list(tuple1)
lst[0] = 'Deeksha'
t = tuple(lst)
print("Tuple after replacing values : ",t)
print("slicing_tuple : ",tuple1[1:4])
del tuple1
print("Deleting tuple : ",tuple1)
