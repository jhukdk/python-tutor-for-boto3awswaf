"""
rules = [
    {"Name": "BlockBadBots", "Priority": 0, "Action": "BLOCK"},
    {"Name": "RateLimit",    "Priority": 1, "Action": "COUNT"},
    {"Name": "AllowHealth",  "Priority": 2, "Action": "ALLOW"},
]

print(rules[0]["Name"])
print(rules[2]["Action"])

BlockBadBots
ALLOW
that bracket notation reaches the 2nd dictionary item then accesses the value associated with the key "Priority"
"""

web_acl = {
    "Name": "prod-acl",
    "Scope": "REGIONAL",
    "Rules": [
        {"Name": "BlockBadBots", "Priority": 0, "Action": "BLOCK"},
        {"Name": "RateLimit",    "Priority": 1, "Action": "COUNT"},
        {"Name": "AllowHealth",  "Priority": 2, "Action": "ALLOW"},
    ],
}

# BlockBadBots
# print(web_acl["Rules"][1]["Action"])

"""
for rule in web_acl["Rules"]:
    if rule["Action"] == "BLOCK":
        print(f"Blocking rule: {rule["Name"]}")
"""

#    if web_acl[Rules][2] == "BLOCK":
#        print(f"Blocking rule: {na}")

response = {
    "WebACLs": [
        {"Name": "prod-acl", "Id": "a1", "Rules": [
            {"Name": "BlockBadBots", "Action": "BLOCK"},
            {"Name": "CountFloods",  "Action": "COUNT"},
        ]},
        {"Name": "dev-acl", "Id": "b2", "Rules": [
            {"Name": "AllowAll", "Action": "ALLOW"},
        ]},
    ]
}


"""
Q1) prod-acl
Q2) print(response["WebACLs"][0]["Rules"][0]["Action"]) #prints "BLOCK"
Q3) for blank in response["WebACLs"]:
        print(blank["Name"])
prints prod-acl and dev-acl on 2 lines
Q4) for blank in response["WebACLs"][0]["Rules"]:
    if blank["Action"] == "COUNT":
        print(blank["Name"])
"""