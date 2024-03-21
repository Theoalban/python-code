import jenkins


def list_jobs():   
    server = jenkins.Jenkins('http://192.168.56.177:8080/', username='Theo', password='vagrant')
    jobs = server.get_jobs() # Get all jobs on the Jenkins Server
    list_of_jobs=[]

    for i in jobs:
        list_of_jobs.append((i['name'], i['url'], i.get('color')))  # Print job name by using square  brackets to access dictionary value, also using get() method for color to handle errors since color is not appearing everywhere
                                                                    # use append()  to add each job name to a list
    return list_of_jobs   #return a list of dictionaries with job name and url as values 
a = list_jobs()
print(a) 
print(type(a))
print(len(a))