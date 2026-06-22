import boto3

client = boto3.client("wafv2", region_name="us-east-1")  # us-east-1 = correct for CloudFront
response = client.list_web_acls(Scope="CLOUDFRONT")

web_acls = response["WebACLs"]
print(f"Found {len(web_acls)} Web ACLs in CLOUDFRONT")

print(response.keys())

for aclname in web_acls:
	print(aclname["Name"])

