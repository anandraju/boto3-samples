#!/bin/python3.7
import boto3
client=boto3.client('ec2')
ec2=boto3.resource('ec2')

# az_instances=[]
# for instance in ec2.instances.filter(Filters=[
#     {
#         'Name': 'availability-zone',
#         'Values':['us-east-2a']
#     }
# ]):
#     az_instances.append(instance.instance_id)
# for each_instance in az_instances:
#     if len(each_instance) >= 1:
#         print(each_instance)
#         client.stop_instances(InstanceIds=[each_instance], Force=True)
    
for instance in ec2.instances.filter(Filters=[
  {
      'Name':'instance-state-name',
      'Values': ['running']
  } 
]):
    print(f'The instance ID ---> \'{instance.instance_id}\' and Instane type is ---> \"{instance.instance_type}\"')

    

"""
#Display Availability-zone instances:
#=====================================
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values':['us-east-2a']
    }
]):

    print(f'The instance ID \'{instance.instance_id}\' and Instane type is \"{instance.instance_type}\"')
"""