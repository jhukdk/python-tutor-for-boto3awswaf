import boto3

client = boto3.client("wafv2", region_name="us-east-1")

IPSET_NAME = "w4-practice"
IPSET_ID = "5cb05cf6-3c35-45f4-9677-c030735fefd6"

# 1. GET — current addresses + a fresh LockToken
got = client.get_ip_set(Name=IPSET_NAME, Scope="CLOUDFRONT", Id=IPSET_ID)
current_addresses = got["IPSet"]["Addresses"]
lock_token = got["LockToken"]
print("Before:", current_addresses)

# 2. MODIFY — append, keeping what's already there
new_addresses = current_addresses + ["198.51.100.0/24"]

# 3. UPDATE — send the FULL list + the LockToken
client.update_ip_set(
    Name=IPSET_NAME,
    Scope="CLOUDFRONT",
    Id=IPSET_ID,
    Addresses=new_addresses,
    LockToken=lock_token,
)
print("After update, sent:", new_addresses)