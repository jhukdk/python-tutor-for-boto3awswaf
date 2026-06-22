import boto3
from botocore.exceptions import ClientError
from pprint import pprint

client = boto3.client("wafv2", region_name="us-east-1")

IPSET_NAME = "w4-practice"
IPSET_ID = "5cb05cf6-3c35-45f4-9677-c030735fefd6"

# GET a token...
got = client.get_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID)
stale_token = got["LockToken"]
addresses = got["IPSet"]["Addresses"]

pprint(stale_token)

# First update SUCCEEDS — this consumes (rotates) the token
client.update_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID,
                     Addresses=addresses, LockToken=stale_token)
print("First update OK. Token is now stale.")

# Second update REUSES the now-stale token -> should be rejected
try:
    client.update_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID,
                         Addresses=addresses, LockToken=stale_token)
    print("Second update OK (unexpected)")
except ClientError as e:
    code = e.response["Error"]["Code"]    # WAFOptimisticLockException
    print("Second update rejected with code:", code)
