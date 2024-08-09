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
    print(f"AWS Region: {session.region_name}")

# in case of an error:
except ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == 'InvalidClientTokenId':
        print("Error: Invalid security token. Check your AWS credentials.")
    elif error_code == 'ExpiredToken':
        print("Error: Expired security token. Please refresh your credentials.")
    else:
        print(f"ClientError: {e}")
    sys.exit(1)

except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
