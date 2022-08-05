#!/usr/bin/env python3

import boto3
import logging

# Connect to AWS client endpoint
client = boto3.client('ec2')

# Set logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Get Addresses
    ids = []
    response = client.describe_addresses()
    for resource in response["Addresses"]:
        if 'AssociationId' not in resource.keys():
            ids.append(resource["AllocationId"])
            
    # Release unassociated EIPs
    for id in ids:
        try:
            response = client.release_address(AllocationId=id)
            print(f"Address: {id} released.")
        except 


lambda_handler(None, None)
