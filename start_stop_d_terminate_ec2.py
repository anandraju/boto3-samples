#!/bin/python3.7
import boto3
client=boto3.client('ec2')

response=client.terminate_instances(InstanceIds=['i-010e8629f8adb5cc4', 'i-0c847270309ac058e'])

for instance in response['TerminatingInstances']:
    print(f"The Instance with id {instance['InstanceId']} Terminated")

'''
response = client.stop_instances(
    InstanceIds=[
        'i-010e8629f8adb5cc4', 'i-0c847270309ac058e',
    ],
    #Hibernate=True|False,
    #DryRun=True|False,
    Force=True
)
'''
#START INSTANCE
# response = client.start_instances(
#     InstanceIds=[
#         'i-010e8629f8adb5cc4', 'i-0c847270309ac058e',
#     ],
#     #Hibernate=True|False,
#     #DryRun=True|False,
#     Force=True
# )
