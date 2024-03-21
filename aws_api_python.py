import boto3 
import csv
filter1  = [{'Name': 'tag:env', 'Values': ['prod']}] #Filter for production environment only




#connect to AWS
def list_aws_instances():
    _ec2 = boto3.client('ec2', region_name= 'us-east-1') #create  an EC2 client object to make API requests to AWS
    response = _ec2.describe_instances(filters=filter1) # call a method  on the ec2 object to get details about instances in your account.
    #print(***********)
    #print(response)
    list_of_instances=[]
    for i in response['Reservations']:
        for j in i['Instances']:
            list_of_instances.append([j['InstanceId'], j['ImageID'], j['InstanceType'], j['LaunchTime'], j['Placement']['AvailabilityZone']])
            
    return(list_of_instances)

with open("list_of_instances.csv", "w", newline="") as f: 
    pen = csv.writer(f)
    header = ["INSTANCE_ID", "IMAGE_ID", "INSTANCE_TYPE", "INSTANCE_LUNCH_TIME", "AVAILABILITY_ZONE"] 
    pen.writerow(header) 
    for a in list_aws_instances():
        pen.writerow(a)
f.close 
