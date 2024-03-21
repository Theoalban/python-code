import csv

# Open the file named 'family1.csv' in write mode and assign it to a variable called 'f'
with open('family1.csv', 'w', newline='') as f:
    # Create an object "c" of the CSV writer class with 'f' assigned to its  'fileobject'
    c = csv.writer(f)

# Define the headers for your CSV file, which are strings stored in a list called 'headers'. These will be written to the first row
    headers = ['Name', 'Age', 'Relation',  'Gender']

# Write the header to  the CSV file using the 'writeheader()' method of 'c'. The argument is a list containing the column names.    
    c.writerow(headers)
     
    # Define a function called 'add_member()' that takes four arguments ('name', 'age', 'relation', 'gender').
    def add_member(name, age, relation, gender):
        """Adds a family member to the list."""
        members = [name, age, relation, gender]
        c.writerow(members)
    
    # Add family members using the function above 
    add_member("Theo", 35, "Father", "Male")
    add_member("John", 30, "Brother", "Male")
    add_member("Jane",  25, "Mother", "Female")
    add_member("Bob",   18, "Son", "Male")
    add_member("Ava",      16, "Daughter", "Female") 

    print("\nThe 'family1.csv' file has been created.") 
    
    # Add Diana as a new family member
    add_member("Diana", 2, "Grand-daughter", "Female")

print("Diana has been added to the family.")





# Now let's add a  new feature - searching for a family member by name  
def search_by_name():
    """Opens the 'family.csv' file, reads all lines, stores them in a list and returns this list."""    
    lines = []
    with open('family.csv','r'   )as s:
        reader=csv.reader(s)
        next(reader)  # Skip the header row
        for row in reader:
            lines.append(row)
            
    return lines

searched_lines = search_by_name()   

# Ask user what they want to look up (either 'Theo', 'John  ', etc.)
lookup = input('\nEnter the name you would like to lookup:\t').strip().lower()

for line in searched_lines:
    if line[0].lower() == lookup:
        print(line)     

