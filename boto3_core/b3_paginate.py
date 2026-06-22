"""
import boto3

client = boto3.client("wafv2", region_name="us-east-1")

paginator = client.get_paginator("list_web_acls")

for page in paginator.paginate(Scope="CLOUDFRONT"):
    for acl in page["WebACLs"]:
        print(acl["Name"])
"""

import boto3

client = boto3.client("wafv2", region_name="us-east-1")

# first page
response = client.list_web_acls(Scope="CLOUDFRONT")
all_acls = response["WebACLs"]

# keep fetching while AWS hands back a NextMarker bookmark
while "NextMarker" in response:
    response = client.list_web_acls(
        Scope="CLOUDFRONT",
        NextMarker=response["NextMarker"],
    )
    all_acls = all_acls + response["WebACLs"]

print(f"Total: {len(all_acls)} CloudFront Web ACLs")
