import boto3

client = boto3.client("wafv2", region_name="us-east-1")

response = client.list_web_acls(Scope="CLOUDFRONT")

for acl in response["WebACLs"]:
    print(acl["Name"], "->", acl["Id"])