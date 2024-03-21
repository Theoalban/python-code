import csv   #importing the csv module

with open("week23.csv", "w", newline="") as f: # Open the file named 'week23.csv' in write mode and assign it to a variable called 'f'
    pen = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL) # Create an object of class csv.writer which will help us write data into the CSV file
    header = ["Name",   "Cell Phone",   "city"] # Define the headers for your CSV file
    pen.writerow(header) # Write the headers to the CSV file
    pen.writerow(["theo", "555-555-5555",  "San Francisco"])  # Write one row of data to the CSV file
    pen.writerow(["Jane", "444-444-4444",  "New York City"])
    pen.writerow(["Jean Doe", "415-555-9876", "Tulsa"])
f.close # Close the file after you are done writing to it

    
with open("week23.csv") as f:  # Open the file in a context manager so it gets closed automatically
    reader = csv.reader(f)  # Create an object called 'reader' that reads from the file
    next(reader)  # Skip     the headers (first line) because we don'   t want them printed
    for row in reader:  # For every row in the CSV file, do this...
        print(row)  # Print out the contents of the row
f.close()

   

