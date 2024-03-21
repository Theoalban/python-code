### voir jenkins_build_job.py for update
import jenkins
import csv


# Trigger a build
def build_and_trigger_job(jenkins_url, jenkins_user, jenkins_pass, job_name):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    server.build_job(job_name)

build_and_trigger_job('http://192.168.56.177:8080/', 'Theo', 'vagrant', 'tk-sample')


def list_jobs(jenkins_url,jenkins_user,jenkins_pass):   
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    jobs = server.get_jobs() # Get all jobs on the Jenkins Server
    list_of_jobs=[]

    for i in jobs:
        list_of_jobs.append((i['name'], i['url'], i.get('color')))  # Print job name by using square  brackets to access dictionary value, also using get() method for color to handle errors since color is not appearing everywhere
                                                                    # use append()  to add each job name to a list
    return list_of_jobs   #return a list of dictionaries with job name and url as 

def jenkins_csv_file(my_list): #define a function called 'jenkins_csv_file' with a parameter  'my_list' which is the output from the list
    with open ("jenkins_iventory1.csv", "w", newline='') as j:
        pen = csv.writer(j)
        header=[ 'Job_Name', 'Job_URL', 'Job_Last_Build_Status']
        pen.writerow(header)
        for item  in my_list:
            pen.writerow(item)
    j.close()
#jenkins_csv_file(list_jobs('http://54.172.51.138:8080','devops','devops')) #We can run it this way 'OR' call 2 different functions as follow
    
jenkins_jobs = list_jobs ('http://192.168.56.177:8080/', 'Theo', 'vagrant') #declaring variable to be used by the function
jenkins_csv_file(jenkins_jobs)


