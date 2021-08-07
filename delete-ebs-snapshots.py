#!/bin/python3.7
from datetime import datetime, timedelta, timezone 
import boto3

ec2=boto3.resource('ec2')
snapshots = ec2.snapshots.filter(OwnerIds=['self'])
for snapshot in snapshots:
    start_time=snapshot.start_time
    delete_time=datetime.now(tz=timezone.utc) - timedelta(days=0)
    if delete_time >= start_time:
        snapshot.delete()
        print(f"The snapshost start_time --> {start_time} and delete_time --> {delete_time}")