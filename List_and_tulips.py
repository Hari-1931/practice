# a = [1,2,3,4,5,6]
# print(a[0])
# print(a[2])
# print(a[-1])
# # Counting of elemenst in a list shoould start from 0,1,2,....etc

# a[0] = 52 
# print(a)
# # List can be modified


# b = [45,'hari',False,3.2]
# # list can be created with diffrent items
# print(b)


# friends = ['me','meagain','my',31]
# print(friends[0:3]) # list slicing..
# print(friends[-2:])




# List methods

# l1= [1,8,7,2,21,15]
# # l1.sort() #sorts the list
# # l1.reverse () reverse the list
# # l1.append(45) # adds athe end of the list
# # l1.insert(0,544) #adds number (2 nd digit) and the given index (1st digit)
# #l1.pop(2) # removes the digit by giving index
# l1.remove(21) # remove the given digit
# print(l1)



# tuples ()
# t = (1,2,4,5)
# print(t[0])

# t[0] = 45 
# tuples are immutable 

# t1 =() #empty tuple
# t2 =(1) # wrong way to declare a tuple with single element
# print(t2)

# t2 = (1,) #correct way to declare a tuple with single element
# print(t2)




# Methods
t1 = (1,2,4,5,3,1,3,5,3,4,1)

print(t1.count(1)) # counts no of specified digit in the tupels
print(t1.index(5)) # searchs the specified digits index in the tupels

