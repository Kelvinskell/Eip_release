#!/usr/bin/env python3

import boto3
import logging

# Connect to AWS client endpoint
client = boto3.client('ec2')

# Set logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
