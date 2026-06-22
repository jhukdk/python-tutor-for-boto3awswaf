import boto3
from pprint import pprint 

client = boto3.client("wafv2", region_name="us-east-1")

WEB_ACL_NAME = "jhuk-tech-cloudfront"
WEB_ACL_ID = "a5276260-d6b8-4f60-9e84-c07ac8eacf76"

response = client.get_web_acl(
    Name=WEB_ACL_NAME,
    Id=WEB_ACL_ID,
    Scope="CLOUDFRONT",
)

web_acl = response["WebACL"]

# print("Default action:", web_acl["DefaultAction"])
# print("Number of rules:", len(web_acl["Rules"]))

pprint(web_acl, indent=2)

"""

print("\nRules (by priority):")
for rule in web_acl["Rules"]:
    name = rule["Name"]
    priority = rule["Priority"]
    action = rule.get("Action", rule.get("OverrideAction"))
    print(f"  [{priority}] {name} -> {action}")


for rule in web_acl["Rules]":
    if rule["Priority"] >= 1:
        print(rule["Name"])
"""