sampled = {
    "SampledRequests": [
        {
            "Request": {"ClientIP": "203.0.113.7", "Country": "US", "URI": "/login", "Method": "POST"},
            "Action": "BLOCK",
            "Weight": 1,
        },
        {
            "Request": {"ClientIP": "198.51.100.4", "Country": "RU", "URI": "/admin", "Method": "GET"},
            "Action": "BLOCK",
            "Weight": 1,
        },
    ],
    "PopulationSize": 1200,
}

for item in sampled["SampledRequests"]:
    req = item["Request"]
    print(f'{item["Action"]} {req["Method"]} {req["URI"]} from {req["ClientIP"]} ({req["Country"]})')