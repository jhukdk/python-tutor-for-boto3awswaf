response = {
    "IPSets": [
        {"Name": "office-allowlist", "Scope": "REGIONAL",   "Addresses": ["203.0.113.4/32", "203.0.113.5/32"]},
        {"Name": "blocklist-emea",   "Scope": "REGIONAL",   "Addresses": ["198.51.100.0/24"]},
        {"Name": "cf-blocklist",     "Scope": "CLOUDFRONT", "Addresses": ["192.0.2.10/32", "192.0.2.11/32", "192.0.2.12/32"]},
    ]
}



def summarize_regional(param): 
    try:
        for num in param["IPSets"]:
            if num["Scope"] == "REGIONAL":
                numberIPs = len(num["Addresses"])
                print(f"{num["Name"]}: {num["Scope"]}: {numberIPs} addresses") 
    except KeyError:
        print("You tried a key that doesn't exist in the response dict")
        
summarize_regional(response)