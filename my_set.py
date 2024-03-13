#set {} Sets in Python are unordered collections of unique elements(duplicates not allow)
#set methods add(), update(), remove(), pop(), clear(), discard()
my_set={-1, 0,1, 2, 3, 4,False,  5, True} #True is equal to 1 and False is equal to 0.
print(f"The set is {my_set}") # is {0, 1, 2, 3, 4, 5} duplicates are removed by python

#Adding an element to a Set using the add() method.
my_set.add(7) 
print(f"The new set is {my_set}")

#Updating a set with use of update () method which can take iterables or another set 

#1-Update with a list:
list1=[8,9,10]
my_set.update(list1)
print(f"Updated set is {my_set}")
#2-Update with another set:  
another_set ={6,11,12}
my_set.update(another_set)
print(f"Updated set after adding another set is {my_set}")
#3-Update with a tuple :
tuple1=(13, 14,15) 
my_set.update(tuple1)
print(f"Updated set after adding a tuple is {my_set}")

#Removing an element from a set using the remove() method
try:   
    my_set.remove(1) #If we try to remove an element that doesn't exist in the set it will raise a KeyError exception #if the element does not exist in the set
except KeyError as e:
    print("Key Error:",e)
print(my_set)

#Using the discard() method instead of remove(). It does not raise an exception if the value is not present.
my_set.discard(15)  
print(my_set)
#We can also use the pop() method to remove and return an arbitrary element from a set.
element=my_set.pop() #it will remove and return any one element from the set.
print(f"Element Removed is {element}")
print(f"New Set After removing Element Using Pop Method is {my_set}")

#clear() method removes all items from the set.
my_set.clear()
print(f"After Clearing The Set it becomes {my_set}")

