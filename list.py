#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert()

print(dir(list))             #To see all methods available for lists

my_list = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1] 
print(len(my_list))    #Return the number of items in the list

#Using append method to add an element at end of the list
my_list.append('docker')  
print(my_list)     #Adding docker at last position
my_list.append('houston')  
print(my_list)      #Adding houston at last position

#Using pop method to remove and return  an item from the end of the list
last_item= my_list.pop()        #Removing and returning the last item
print("The removed item is : ", last_item)       #Printing the removed item
print(my_list)                 #Printing the updated list after removing the item

'''#Using clear method to remove all the elements from the list
#my_list.clear()               #Clearing the entire list
print(my_list)                #Printing empty list
'''
#Using copy method to create a new list with the same elements as the original list
new_list = my_list.copy()         #Creating a new list using copy method
print(new_list)            #Printing the New List

#Changing an existing item in the list
index = my_list.index('devops')          #Finding the index of 'devops'
my_list[index]='cybersecurity'           #Replacing 'devops' with 'cybersecurity'
print(my_list)             #Printing the modified list

#Inserting an item at specific location in the list
position = 3
insertion_value = "cloud"
my_list.insert(position, insertion_value)    #Inserting cloud at 3rd position
print(my_list)

my_list[0] = "Terraform"         #Modifying the first value
print(my_list)              #Printing the modified list

print(my_list[2].upper())    #Converting third value to uppercase

#Extending one list into another
extended_list = ["kubernetes", "Docker-compose"]
my_list.extend(extended_list)
print(my_list)                  #Printing the modified list

#Reversing the order of items in the list
my_list.reverse()
print(my_list)                  #Printing the reversed list

#Sorting the list
my_list2 = ['python', 'java', 'c++']
my_list3 = [1, 5, 4, 8, 6]
my_list2.sort()
my_list3.sort()
print(my_list2)                   #Printing the sorted list
print(my_list3)                   #Printing the sorted list

#Removing all occurrences of a particular item from the list (using remove method)
item_to_remove = 'devops'
while item_to_remove in my_list:     #Checking if devops is present in the list or not
    my_list.remove(item_to_remove)   #If yes, then removing it
print(my_list)                       #Printing the list after removal

#Removing all occurrences of a particular item using list comprehension
my_list = [i for i in my_list if i != 1]         #Filtering out any occurrence of '1'
print(my_list)                               #Printing the filtered list

#Finding the index of a particular item in the list
index_of_element = my_list.index('Terraform')  #Returns the index of terraform in the list
print("The element 'Terraform' is found at index : ", index_of_element)

#Counting the number of times an item appears in the list
count_of_elements = my_list.count(2)      #Returns the count of 2 in the list
print("Number of times '2' occurs in the list : ", count_of_elements)

#Accessing elements through slicing
slice_list = my_list[1:4]                #From second element till fourth element
print(slice_list)                        #Printing the slice list

#Accessing individual characters of string using indexing
string1 = "Hello World"
print(string1[0])                          #Printing first character of the string

#Accessing multiple characters using slicing
multi_characters = string1[0:5]             #From first character till fifth character
print(multi_characters)                                      #Printing the multi-character string

#Reversing a string using slicing
reversed_string1 = string1[::-1]              #Reverse the complete string
print(reversed_string1)

#Concatenating strings
concatenated_string = string1 + " DevOps"
print(concatenated_string)

#Duplicating a string
duplicate_string = string1 *  3            #Replicates the string thrice
print(duplicate_string)
#Capitalizing the first letter of each word in a sentence
sentence = "this is a python tutorial"
capitalized_words = sentence.title()
print(capitalized_words)

#Making acronym from a full name
fullname = "John Doe"
acronym = fullname.split()               #Splitting the full name into words
print(" ".join([i[0] for i in acronym]))    #Creating acronym by taking first letter of each word

#Sorting a list
my_list = [6, 9, 3, 1, 7, 8, 2, 5,  4]     #List to be sorted
sorted_list = sorted(my_list)           #Sorting the list
print(sorted_list)

#Checking if an item exists in a list
item_to_search = 7
if item_to_search in my_list :
    print("Item found")
else:
    print("Item not found")
    #Finding index of an item in a list
index_of_item = my_list.index(item_to_search)
print("Index of the item is ",index_of_item)    

#Removing items from a list
remove_items = [1,   7]                       #Items to remove
removed_items = [x for x in my_list if x not in remove_items ]      #Filter out the items which are present in remove_items list
new_list = [x for x in my_list if x not in remove_items]      #Filter out the unwanted items
print(new_list)





