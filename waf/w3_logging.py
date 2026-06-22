import boto3
from botocore.exceptions import ClientError

client = boto3.client("wafv2", region_name="us-east-1")

WEB_ACL_ARN = "arn:aws:wafv2:us-east-1:877995959706:global/webacl/jhuk-tech-cloudfront/a5276260-d6b8-4f60-9e84-c07ac8eacf76"  # the ARN from response["WebACL"]["ARN"]

try:
    config = client.get_logging_configuration(ResourceArn=WEB_ACL_ARN)
    destinations = config["LoggingConfiguration"]["LogDestinationConfigs"]
    print("Logging is ON. Destination(s):", destinations)
except ClientError as e:
    code = e.response["Error"]["Code"]
    if code == "WAFNonexistentItemException":
        print("Logging is NOT configured for this Web ACL.")
    else:
        raise