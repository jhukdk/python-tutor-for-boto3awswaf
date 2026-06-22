import json
"""
web_acl = {"Name": "prod-acl", "Scope": "REGIONAL", "Rules": ["rate-limit", "geo-block"]}

print(web_acl)                      # cramped — the raw dict
print(json.dumps(web_acl, indent=2))  # pretty — readable JSON text


raw = '{"Name": "prod-acl", "DefaultAction": "Block", "Priority": 0}'

print(type(raw))          # what is it before parsing?

config = json.loads(raw)
print(type(config))       # what is it after parsing?
print(config["DefaultAction"])  # now you can index by key
"""

config = {"Name": "prod-acl", "Scope": "REGIONAL"}

try: 
	print(config["Priority"])
except KeyError:
    print("No Priority key found — using default 0")

print("Script keeps running.")

config2 = {"Name": "prod-acl"}

try:
    print(confg2["Name"])     # typo: confg2, not config2
except:
    print("Something went wrong")   # hides the REAL bug

acl = {"Name": "prod-acl"}
try:
	print(acl["Scope"])
except KeyError:
	print("key missing")


1.) dumps converts a dict into a json string, whereas loads converts a json string to a dict
2.) a string formatted nicely with the contents of data 
3.) indent=2 argument adds spacing to a nested list in within the dictionary
4.) 
acl = {"Name": "prod-acl"}
try:
	print(acl["Scope"])
except KeyError:
5.) specifying the errorType allows other unexcepted ErrorCodes to surface