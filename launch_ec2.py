#!/bin/python3.7
import boto3
client=boto3.client('ec2')
resp=client.run_instances(ImageId='ami-0443305dabd4be2bc',InstanceType='t2.micro',MaxCount=1,MinCount=1)
for instance in resp['Instances']:
    print(instance['InstanceId'])