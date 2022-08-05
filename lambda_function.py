#!/usr/bin/env python3

import boto3
import logging
from botocore.exceptions import ClientError

# Connect to AWS client endpoint
client = boto3.client('ec2')

# Set logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Function {} has started execution.")
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
            logger.info(f"Function {context.function_name}: EIP Address: {id} released.")
        except ClientError as e:
            print(e)

    if not ids:
        logger.info(f"Function {context.function_name}: No unassociated elastic IP address found.")

    logger.info("Function {} has finished execution".format(context.function_name))


