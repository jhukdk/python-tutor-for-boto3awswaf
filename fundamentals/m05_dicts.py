"""
rule = {
    "Name": "BlockBadBots",
    "Priority": 0,
    "Action": "BLOCK",
}
"""

# print(rule["Name"])
# print(rule["Priority"])

# "BlockBadBots"
# 0
# The difference is lists are indexed and dicts rely on names to be accessed and cannot be accessed by index. 

#print(rule.get("Action"))
#print(rule.get("Description"))
#print(rule.get("Description", "none set"))
#print(rule["Description"])

"""
for key in rule.keys():
    print(key)

for value in rule.values():
    print(value)

for key, value in rule.items():
    print(f"{key} = {value}")
"""

"""
ip_set = {
    "Name": "OfficeIPs",
    "Scope": "REGIONAL",
    "Addresses": ["203.0.113.0/24", "198.51.100.10/32"],
}

print(ip_set["Name"])
print(ip_set.get("Description", "none"))

for key, value in ip_set.items():
    print(f"{key} = {value}") 
"""

"""
Q1) 100
Q2) Accessing a dict by name using bracket notation results in a KeyError and breaks the script. Whereas accessing a dict using the .get method returns None and allows the script to continue running.
Q3) dict.items() and this requires 2 loop variables 
Q4) 
rule = {
    "Name": "RateLimit", 
    "Action": "COUNT",
}
print(rule.get("Priority", 0))
"""