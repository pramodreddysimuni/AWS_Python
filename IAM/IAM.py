import boto3


iam =boto3.client('iam')

responce=iam.create_user(
    UserName="pramod_reddy"
)

print(responce)