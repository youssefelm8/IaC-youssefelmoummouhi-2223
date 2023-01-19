import json
with open ('Workshop/Docker Response Data/Docker Example 1: Docker Images Response Data/docker1.json', 'r') as docker_json_file:
    docker_dict = json.load (docker_json_file)
    
print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
print(docker_dict[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json = json.dumps(docker_dict)
print("---------3--------")
print("Filtering from dict")
print(docker_dict[0]["Created"])
print(docker_dict[0]["Architecture"])
print(docker_dict[0]["Os"])