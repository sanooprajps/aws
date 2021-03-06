#!/usr/bin/python
import boto3
import json
import datetime

# Python3 is required to run this program
# Describe EC2 instance
######################################
# custom handler convert datetime inside json to string value
######################################
def datetime_handler(awsResponse):
    if isinstance(awsResponse, datetime.datetime):
        return awsResponse.isoformat()

######################################
# List of EC2 instance
######################################
def instanceList(response_json):
    ec2_instance = []
    for reservation in response_json['Reservations']:
        for instance in reservation['Instances']:
            ec2_instance.append(instance['InstanceId'])
    return ec2_instance
######################################
# MAIN function
######################################
if __name__ == "__main__":
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
# For pretty view of response json, uncomment following line
#    print (json.dumps(response, indent=4, sort_keys=True, default=datetime_handler))
# AWS response contains datetime where json can't understand this. 
    response_d = json.dumps(response, default=datetime_handler)
    response_json = json.loads(response_d)
    ec2_instance = instanceList(response_json)
    print ("EC2 instance summary received. Number of instance available :- {}".format(ec2_instance))
