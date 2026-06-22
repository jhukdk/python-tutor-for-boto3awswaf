import boto3
from datetime import datetime, timezone, timedelta

cw = boto3.client("cloudwatch", region_name="us-east-1")

now = datetime.now(timezone.utc)

stats = cw.get_metric_statistics(
    Namespace="AWS/WAFV2",
    MetricName="AllowedRequests",
    Dimensions=[
        {"Name": "WebACL", "Value": "jhuk-tech-cloudfront"},
        {"Name": "Rule", "Value": "jhuk-tech-common-rule-set"},
        {"Name": "Region", "Value": "CloudFront"},
    ],
    StartTime=now - timedelta(hours=3),
    EndTime=now,
    Period=3600,
    Statistics=["Sum"],
)

print("Datapoints:", stats["Datapoints"])

