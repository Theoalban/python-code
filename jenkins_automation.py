# First install the jenkins module with "$pip install python-jenkins"

#  Import modules.
import jenkins 

# Initialize Jenkins server connection
jenkins_url = 'http://192.168.56.177:8080/'   # URL for your Jenkins Server (must end in a '/')....
my_username = 'Theo'
my_password = 'vagrant' #You can also create a token on your jenkins server  instead of password if you prefer.

server = jenkins.Jenkins(jenkins_url, username=my_username, password=my_password)     # Connect to Jenkins Server.

#user = server.get_whoami()          # Return information about the logged in user.
#print(user['fullName'])

version=server.get_version()        # Get the version of Jenkins running on the server.
print(f'The Jenkins Version is  {version}')

# Example1: Trigger a build
job_name = 'job-sample' # Name of an existing job you wish to trigger.
server.build_job(job_name)  # Builds the job named "job-sample".( or  server.build_job('job-sample')  , if you prefer )

job_name2 = 'first-job' # Name of job you wish to trigger.
server.build_job(job_name2)  # Builds the job named "first-job".
job_info = server.get_job_info(job_name2) # Gets info about the specified job......
build_number = job_info['lastBuild']['number']  # Get the number of the last build.....
print('Last build for first-job was job number', build_number)            # Print out the number of the last build.
print('Triggering', job_name2, build_number)  # Display job name and build number

# Example2: 
#server.create_job("job1",jenkins.EMPTY_CONFIG_XML)     # Create an empty job called "job1"

#delete an existing  Job
server.delete_job("job3")
print("Existing job 'job3' deleted successfully.")

# Example3: create a job with a  config file (preconfigure job)
job3_xml = open("job3.xml" ,mode="r" ,encoding='utf-8').read()  # Read the XML from a local file.
server.create_job("job3", job3_xml)
print("Job3 created successfully.")
server.build_job('job3')  # Builds the job named "job3".
print("Job3 built successfully.")

# Example4: Get all  jobs on the server
all_jobs = server.get_all_jobs()    # Returns a dictionary of {job name : <jenkins.job.Job>} or (server.get_jobs)
print(all_jobs)

# Example5: Copy job
#server.copy_job('source_jobName',  'target_jobName')

# Example6: update  job configuration
#update_job_3 =open("job_3_updated.xml", mode= 'r', encoding='utf-8')   # Open the updated xml file
#server.reconfig_job('job3', update_job_3)

#disable job
#server.disabe_job('job1')











#build_number = server.create_job(job_name)['nextBuildNumber'] - 1             # Get latest available build number
#build_number = server.get_job_info(job_name)['nextBuildNumber'] - 1           # Get latest available build number.

