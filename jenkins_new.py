import jenkins
import csv

jenkins_url = 'http://192.168.56.177:8080/'  # Define at global scope
jenkins_user = 'Theo'  # Define at global scope
jenkins_pass = 'vagrant'  # Define at global scope

def list_jobs():
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    jobs = server.get_jobs()
    list_of_jobs = []

    for i in jobs:
        list_of_jobs.append((i['name'], i['url'], i.get('color')))
    
    return list_of_jobs

def jenkins_csv_file(my_list):
    with open("jenkins_inventory10.csv", "w", newline='') as j:
        pen = csv.writer(j)
        header = ['Job_Name', 'Job_URL', 'Job_Last_Build_Status']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)

def create_and_build_job(job_name, config_xml):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    server.create_job(job_name, config_xml)
    server.build_job(job_name)

def start_job(job_name):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    server.build_job(job_name)

def main():
    # Create and build a new job
    new_job_name = 'job10'
    new_job_config_xml = 'job10.xml'
    create_and_build_job(new_job_name, new_job_config_xml)

    # Start an existing job
    existing_job_name = 'job3'
    start_job(existing_job_name)

    # List existing jobs
    jenkins_jobs = list_jobs()
    jenkins_csv_file(jenkins_jobs)

if __name__ == "__main__":
    main()
