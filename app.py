import boto3
import sys
from botocore.exceptions import ClientError

try:
    session = boto3.Session()
    # Get Account ID
    account_id = session.client('sts').get_caller_identity().get('Account')    
    
    # Get User Information
    user_info = session.client('sts').get_caller_identity()
    
    # Print out all the info    
    print(f"AWS Account ID: {account_id}")
    print(f"User ID: {user_info['UserId']}")
    print(f"Arn: {user_info['Arn']}")
    # Does not print region, just Region: region
    # Fixing region argument to print
    print(f"Region: {region}")

# in case of an error:
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'InvalidClientTokenId':
        print("An error occurred: The security token included in the request is invalid. You should probably check the AWS access key and secret environment variables.")
    elif error_code == 'ExpiredToken':
        print("An error occurred: The security token included in the request has expired. You should refresh your credentials.")
    else:
        print(f"An error occurred: {e}")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
