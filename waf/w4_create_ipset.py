import boto3

client = boto3.client("wafv2", region_name="us-east-1")

response = client.create_ip_set(
    Name="w4-practice",
    Scope="CLOUDFRONT",
    IPAddressVersion="IPV4",
    Addresses=["192.0.2.0/24"],
    Description="W4 practice set - safe to delete",
)

summary = response["Summary"]
print("Created IP set:")
print("  Name:", summary["Name"])
print("  Id:", summary["Id"])
print("  LockToken:", summary["LockToken"])