# Eip_release
A Python Script for an AWS lambda function that finds and releases unassociated Elastic IP Addresses

This is a very short and sweet python script that traverses your AWS accounts to find and release any unassociated Elastic IP Addresses.
I got the inspiration to write this script after i was charged overnight by AWS for keeping unassociated Ip addresses.

This script is designed to be built into a lambda function, so that it can run at specified intervals, according to whatever triggers set for the lambda function.

# Usage
To use this script:
- Clone this repo.
- Navigate to the directory and execute the following AWS CLI command to create your lambda function:
  - `aws lambda create-function --function-name Eip_release --zip-file file://lambda_function.py.zip --handler lambda_handler --role "Your-IAM-role" --runtime python3.8`
- You will need to set the appropriate trigger for your lambda function, according to your needs.

