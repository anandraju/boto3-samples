#!/bin/python3.7
import boto3
sns_client=boto3.client('sns')

ec2=boto3.resource('ec2')
backup_filter=[
    {
        'Name':'tag:Backup',
        'Values': ['Yes']
    }
]

snapshot_ids=[]
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot=vol.create_snapshot(Description='Craeted by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)
        print(snapshot_ids)

sns_client.publish(
    TopicArn = 'arn:aws:sns:us-east-2:810131116727:snapshots',
    Subject = 'EBS Snapshots',
    Message = str(snapshot_ids)
)