import jenkins
import csv

def list_jobs(jenkins_url, jenkins_user, jenkins_pass):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    jobs = server.get_jobs()  # Get all jobs on the Jenkins Server
    list_of_jobs = []

    for i in jobs:
        list_of_jobs.append((i['name'], i['url'], i.get('color')))  # Print job name by using square brackets to access dictionary value, also using get() method for color to handle errors since color is not appearing everywhere
        # use append() to add each job name to a list
    return list_of_jobs  # return a list of dictionaries with job name and url as values


def jenkins_csv_file(my_list):  # define a function called 'jenkins_csv_file' with a parameter 'my_list' which is the output from the list
    with open("jenkins_inventory1.csv", "w", newline='') as j:
        pen = csv.writer(j)
        header = ['Job_Name', 'Job_URL', 'Job_Last_Build_Status']
        pen.writerow(header)
        for item in my_list:
            pen.writerow(item)


def create_and_build_job(jenkins_url, jenkins_user, jenkins_pass, job_name, config_xml):
    server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    server.create_job(job_name, config_xml)  # Create a new job
    server.build_job(job_name)  # Build the new job


# Main function to list jobs, create a new job, and build it
def main():
    jenkins_url = 'http://54.172.51.138:8080'
    jenkins_user = 'devops'
    jenkins_pass = 'devops'

    # List existing jobs
    jenkins_jobs = list_jobs(jenkins_url, jenkins_user, jenkins_pass)
    jenkins_csv_file(jenkins_jobs)

    # Create and build a new job
    new_job_name = 'NewJob'
    new_job_config_xml = """<your_job_configuration_here>"""  # Replace with your job configuration XML
    create_and_build_job(jenkins_url, jenkins_user, jenkins_pass, new_job_name, new_job_config_xml)


if __name__ == "__main__":
    main()