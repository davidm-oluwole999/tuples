#lists are mutable, tuples are immutable#

list1= [2,3,4,5,6]
tuple1= (2,3,4,5,6)

list1[2]= 10
print(list1)

print(tuple1[2])

#tuple1[2]= 10
print(tuple1)

#length of a tuple
print(len(tuple1))

#Positive indexing
print(tuple1[2])

#Negative indexing
print(tuple1[-3])

print(".......")

#positive sclicing
print(tuple1[0:3])
print(tuple1[:3])
print(tuple1[2:])

#negative sclicing
print(tuple1[-3:-1])
print(tuple1[:-3])
print(tuple1[-2:])

#reverse order
print(tuple1[::-1])

#Packing
fruits= ("apple","banana","cherry")

#Unpacking
(a,b,c)= fruits

print(a)
print(b)
print(c)
#tuple without parenthesis
tuple2= 3,4.6,"chicken",False

print(tuple2)

#nested tuple
tuple3=("food",[1,2,3,4],(10,20,30,40),(11,22,33,44))
print(tuple3[2][2])