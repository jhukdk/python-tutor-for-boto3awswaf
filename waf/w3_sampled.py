import boto3

client = boto3.client("wafv2", region_name="us-east-1")

WEB_ACL_NAME = "jhuk-tech-cloudfront"
WEB_ACL_ID = "a5276260-d6b8-4f60-9e84-c07ac8eacf76"

response = client.get_web_acl(Name=WEB_ACL_NAME, Id=WEB_ACL_ID, Scope="CLOUDFRONT")
web_acl_arn = response["WebACL"]["ARN"]

for rule in response["WebACL"]["Rules"]:
    metric_name = rule["VisibilityConfig"]["MetricName"]
    print(rule["Name"], "-> metric:", metric_name)

from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)

sampled = client.get_sampled_requests(
    WebAclArn=web_acl_arn,
    RuleMetricName="jhuk-tech-rate-limit",
    Scope="CLOUDFRONT",
    TimeWindow={
        "StartTime": now - timedelta(hours=3),
        "EndTime": now,
    },
    MaxItems=100,
)

print("Sampled requests returned:", len(sampled["SampledRequests"]))


print(web_acl_arn)

