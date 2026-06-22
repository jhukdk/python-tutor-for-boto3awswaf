# variables.py

# Strings (str) — names, ARNs, and IDs in AWS are all strings
web_acl_name = "prod-frontend-acl"
scope = "REGIONAL"              # WAF scope is either "REGIONAL" or "CLOUDFRONT"

# Integers (int) — rule priorities, limits, counts
rule_priority = 10
blocked_request_count = 4521

# Booleans (bool) — flags and toggles
sampled_requests_enabled = True

# Printing values
print(web_acl_name)
print("Priority:", rule_priority)

# f-strings: the cleanest way to build readable output.
# Note the f before the quote; anything in {curly braces} gets filled in.
print(f"Web ACL '{web_acl_name}' uses scope {scope} with {blocked_request_count} blocked requests.")

# Inspecting a value's type
print(type(web_acl_name))            # <class 'str'>
print(type(rule_priority))           # <class 'int'>
print(type(sampled_requests_enabled))# <class 'bool'>