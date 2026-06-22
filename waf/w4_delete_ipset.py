import boto3

client = boto3.client("wafv2", region_name="us-east-1")

IPSET_NAME = "w4-practice"
IPSET_ID = "5cb05cf6-3c35-45f4-9677-c030735fefd6"

# GET a fresh lock token right before the delete
got = client.get_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID)

lock_token = got["LockToken"]

client.delete_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID, LockToken=lock_token)
print("Deleted IP set:", IPSET_NAME)