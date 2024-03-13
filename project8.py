import boto3

_iam = boto3.client('iam')

users = _iam.list_users()

for i in users['Users']:
    print(i['UserName'])