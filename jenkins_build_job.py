####   TRES BON!!!
import jenkins
import csv

# Initialize Jenkins server connection
jenkins_url = 'http://192.168.56.177:8080/'   # URL for your Jenkins Server (must end in a '/')....
jenkins_user = 'Theo'
jenkins_pass = 'vagrant' #You can also create a token on your jenkins server  instead of password if you prefer.
server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)     # Connect to Jenkins Server.

# Example1: Trigger a build
def  trigger_build():
    job_name = 'job3' # Name of an existing job you wish to trigger.
    server.build_job(job_name)  # Builds the job named "job-sample".( or  server.build_job('job-sample')  , if you prefer )
trigger_build()
'''
# Example3: create and build a new job with a  config file (preconfigure job)
def preconfig_new_job():
    job10_xml = open("job10.xml" ,mode="r" ,encoding='utf-8').read()  # Read the XML from a local file.
    server.create_job("job10", job10_xml)
    server.build_job('job10')  # Builds the job named "job10".
preconfig_new_job()
'''

def  list_jobs():
    jobs = server.get_jobs()
    list_of_jobs =[]

    for i in jobs:
        list_of_jobs.append((i['name'], i['url'], i.get('color')))  # Print job name by using square brackets to access dictionary value, also using get() method for color to handle errors since color is not appearing everywhere
        # use append() to add each job name to a list
    return list_of_jobs  # return a list of dictionaries with job name and url as values
a = list_jobs()
#print(a)
print(type(a))
print(len(a))

def jenkins_csv_file(my_list):  # define a function called 'jenkins_csv_file' with a parameter 'my_list' which is the output from the list
    with open("jenkins_inventory10.csv", "w", newline='') as j:
        pen = csv.writer(j)
        header = ['Job_Name', 'Job_URL', 'Job_Last_Build_Status']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)
    j.close


#jenkins_csv_file(list_jobs('http://192.168.56.177:8080','Theo','vagrant')) #We can run it this way 'OR' call 2 different functions as follow
    
jenkins_jobs = list_jobs () #declaring variable to be used by the function
jenkins_csv_file(jenkins_jobs)
   