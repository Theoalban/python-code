import boto3
#from botocore.exceptions import ClientError

#filter _name = 'tag:Name'  
_value = "EC2-Instance"  # replace with your tag value if different 

#AWS_REGION= "<REGION_NAME>"
_ec2 = boto3.client('ec2', region_name="us-east-1")
resp =  _ec2.describe_instances()
for i in resp['Reservations']:
    for j in i['Instances']:
        print(j)
        
def get_instance_info():
    """Return a list of dictionaries containing instance information"""
    
    instances = []
    for r in resp['Reservations']:
        for i in r['Instances']:
            # Create a dictionary with the essential info about each instance and add it to our list
            instances.append({'InstanceID':i['InstanceId'], 'State':i[' State']['Name'], \
                             'PublicIP':i['PublicIpAddress'],    
                              'PrivateIP':i['Private    IpAddress'],\
                               })
    return instances


'''
buckets_list = s3_client.list_buckets()

# get a list of bucket's names
buckets = []
for bucket in buckets_list['Buckets']:
    buckets.append(bucket['Name'])

def get_unencrypted_buckets():
    """ This function get a list of all s3 buckets without Encryption """
    unencrypted_buckets=[]
    encryptionError='ServerSideEncryptionConfigurationNotFoundError'
    for bucket in buckets:
        try:
            # bucket has encryption enable
            bucket_enc_response = s3_client.get_bucket_encryption(Bucket=bucket) 
            rules = bucket_enc_response['ServerSideEncryptionConfiguration']['Rules']
            print(f"Bucket: {bucket}, Encryption: {rules}")
        except ClientError as e:
            if e.response['Error']['Code'] == encryptionError: # unencrypted bucket error
                print(f"Bucket: {bucket}, no server-side encryption")
                unencrypted_buckets.append(bucket) # add unencrypted bucket in a list
            else: # any other type of error
                print(f"Bucket: {bucket}, unexpected error for encryption check: {e}")
    return unencrypted_buckets

def get_nopolicy_buckets():
    """ This function get a list of all s3 buckets without policy"""
    no_policy_buckets=[]
    policyError= 'NoSuchBucketPolicy'
    for bucket in buckets:
        try:
            # bucket has policy
            policy_status=s3_client.get_bucket_policy_status(Bucket=bucket)
            print(f"Bucket: {bucket}, policy: {policy_status}")
        except ClientError as e:
            if e.response['Error']['Code'] == policyError: # no policy bucket error
                print(f"Bucket: {bucket}, has no policy attached")
                no_policy_buckets.append(bucket) # add no policy bucket in a list
            else:# any other type of error
                print(f"Bucket: {bucket}, unexpected error for policy check: {e}")
    return no_policy_buckets

if __name__ == "__main__":
  unencrypted_buckets= get_unencrypted_buckets()
  no_policy_buckets= get_nopolicy_buckets()
  exposed_buckets=list(set(unencrypted_buckets+no_policy_buckets))
  print("################### List of exposed buckets #########################")
  print(exposed_buckets)
  '''