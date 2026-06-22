"""
def block_count(rule):
    return rule["Name"]

rule = {"Name": "RateLimit", "Action": "Block"}
result = block_count(rule)
print(result)

def block_count(rule):
    rule["Name"]          # no return — the value is computed then thrown away

rule = {"Name": "RateLimit", "Action": "Block"}
print(block_count(rule))

"""

def blocking_rule_names(web_acl):
    blocked = []
    for rule in web_acl["Rules"]:
        if rule["Action"] == "Block":
            blocked.append(rule["Name"])
    return blocked

acl = {
    "Name": "prod-acl",
    "Rules": [
        {"Name": "RateLimit", "Action": "Block"},
        {"Name": "AllowHealthCheck", "Action": "Allow"},
        {"Name": "SQLiRule", "Action": "Block"},
    ],
}

print(blocking_rule_names(acl))

def rule_names_by_action(web_acl, action="Block"):
    matches = []
    for rule in web_acl["Rules"]:
        if rule["Action"] == action:
            matches.append(rule["Name"])
    return matches

acl = {
    "Name": "prod-acl",
    "Rules": [
        {"Name": "RateLimit", "Action": "Block"},
        {"Name": "AllowHealthCheck", "Action": "Allow"},
        {"Name": "SQLiRule", "Action": "Block"},
        {"Name": "GeoWatch", "Action": "Count"},
    ],
}

print(rule_names_by_action(acl))
print(rule_names_by_action(acl, "Count"))
print(rule_names_by_action(acl, action="Allow"))

"""
1) 
"CLOUDFRONT in us-east-1"
"REGIONAL in eu-west-1"
2) This function implicitly returns None which is NoneType.
3) 
def count_rules(web_acl):
    howmany = len(web_acl["Rules"])
    return howmany
4) It matters for code script maintainability. If I need to make a change to loop logic, I only need to change the function in one place. 
"""