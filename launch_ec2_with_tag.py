#!/bin/python3.7
import boto3
client=boto3.client('ec2')

resp=client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']
}])


instance_ids=[]
instance_zone=[]

for zone_instance in client.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values':['us-east-2a']
    }
]):
    instance_zone.append(zone_instance.instance_id)


for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        #print(instance['InstanceId'])
        #print(f"Instance Id is {instance['InstanceId']}")
        instance_ids.append(instance['InstanceId'])
        
if instance_ids == instance_zone:
    
        tag_cration = client.create_tags(
            Resources = instance_ids,
            Tags = [
                {
                    'key':'tag:Type',
                    'Value': 'Scheduled'
                }
                ]
        )