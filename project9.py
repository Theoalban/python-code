import jenkins

# 'http://69.164.196.248:8080/' is the ip address of the jenkins server
_con = jenkins.Jenkins('http://192.168.56.177:8080/', username='theo', password='theo')
jenkins_user = _con.get_whoami()
jenkins_version = _con.get_version()
job_number = _con.jobs_count()
jobs_name =_con.get_all_jobs()

print(f" Total number of jobs is: {job_number}")
print("\n Below is the list of all jobs in jenkins and thier url \n")
for i in jobs_name:
    
    print(i['name'] + "  " + i['url'])