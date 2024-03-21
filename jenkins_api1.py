
import jenkins
import os
import csv
# Connect to Jenkins server by creating an object
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
# Create and write to CSV file
with open('jenkins_jobs.csv', 'w', newline='') as csvfile:
    fieldnames = ['Job Name', 'Job URL', 'Job Color', 'Job Fullname'] #
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for job in jobs:
        writer.writerow({'Job Name': job['name'],
                         'Job URL': job['url'],
                         'Job Color': job.get('color', 'Not Available'),
                         'Job Fullname': job['fullname']})
csvfile.close
