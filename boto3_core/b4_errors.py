import boto3
from botocore.exceptions import ClientError

client = boto3.client("wafv2", region_name="us-east-1")

try:
    respo = client.get_web_acl(
        Name="this-does-not-exist",
        Scope="CLOUDFRONT",
        Id="00000000-0000-0000-0000-000000000000",
    )
    print(respo["WebACL"]["Name"])
except ClientError as e:
    code = e.response["Error"]["Code"]
    if code == "WAFNonexistentItemException":
        print(f"No such Web ACL — check the name, Id, and scope.")
    elif code == "AccessDeniedException":
        print(f"Permission denied — your role can't do this. IAM issue.")
    elif code == "ExpiredTokenException":
        print(f"Your SSO session expired. Run: aws sso login.")
    else:
        print(f"The unexpected raw code is {code}")    