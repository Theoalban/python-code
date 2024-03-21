
###### A REVOIR

import jenkins
import os
import csv
# Connect to Jenkins server
server = jenkins.Jenkins('http://54.172.51.138:8080', username='devops', password='devops')

# Get current user information
user_info = server.get_whoami()

# Extract and print the username
username = user_info['id']
print("Current User:", username)

# Get Jenkins version
version = server.get_version()

#  Jenkins version
print("Jenkins Version:", version)

#print(dir(server))

os.system('clear')

job_number= server.jobs_count()
node_list= server.get_nodes()
jobs= server.get_all_jobs()
#print(job_number)
#print(node_list)
#print(jobs)
for job in jobs:
         print("")
         print("")
         print("Job Name:", job['name'])
         print("Job URL:", job['url'])
         print("Job Fullname:", job['fullname'])
         # Check if 'color' attribute exists
         if 'color' in job:
            print("Job Color:", job['color'])
         else:
           print("Job Color: Not Available")

with open("jenkins_jobs_sample.csv", "w", newline="") as csvfile1: # Open the file named 'jenkins_jobs_sample.csv' in write mode and assign it to a variable called 'csvfile'
    header = ['Job Name', 'Job URL', 'Job Color', 'Job Fullname'] # Define the headers for your CSV file
    pen = csv.writer(csvfile1, header=header) # Create an object of class csv.writer which will help us write data into the CSV file
   
    

    pen.writeheader()
    for job in jobs:
        pen.writerow({'Job Name': job['name'],
                         'Job URL': job['url'],
                         'Job Color': job.get('color', 'Not Available'),
                         'Job Fullname': job['fullname']})
csvfile1.close()





