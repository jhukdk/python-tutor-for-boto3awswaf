# m03_loops.py — Loops
# Type each snippet yourself, then run the file to see the output.
rules = ["block-sqli", "rate-limit", "geo-block"]

for rule in rules:
    print(rule)

scopes = ["REGIONAL", "CLOUDFRONT"]
actions = ["Allow", "Block"]

for scope in scopes:
    for action in actions:
        print(f"{scope} - {action}")

priorities = [10, 20, 30]
for i in priorities:
	print(i)

for j in range(5):
	print(j)

"us-east-1 #0"
"us-east-1 #1"
"eu-west-1 #0"
"eu-west-1 #1"
