import boto3

regional_client = boto3.client("wafv2", region_name="us-east-1")
cloudfront_client = boto3.client("wafv2", region_name="us-east-1")

print(f"regional_client → Scope='REGIONAL' | cloudfront_client → Scope='CLOUDFRONT'")