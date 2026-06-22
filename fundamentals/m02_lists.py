# m02_lists.py — Lists
# Type each snippet yourself, then run the file to see the output.
rules = ["block-sqli", "rate-limit","geo-block"]
print(rules)
print(rules[0])
print(rules[1])
print(len(rules))
print(rules[-1])
rules.append("allow-healthcheck")
print(rules)
print(len(rules))
print(rules[4])

regions = ["us-east-1", "us-west-2", "eu-west-1"]
print(regions[1])
regions.append("asia-central-4")
print(len(regions))
# regions[4] would raise IndexError because the highest index in the current regions list is 3