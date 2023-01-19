import json
with open ('Workshop/Docker Response Data/Docker Example 2: Docker Network Response Data/docker2.json', 'r') as docker_json_file2:
    docker_dict2 = json.load (docker_json_file2)

print("---------1--------")
print("Converting json string to dict, and showing keys at level 1")
print(docker_dict2[0].keys())
print("---------2--------")
print("Converting dict to raw json")
docker_json2 = json.dumps(docker_dict2)
print("Filtering from dict")
print(docker_dict2[0]["Name"])
print(docker_dict2[0]["Created"])
print(docker_dict2[0]["Containers"]["4e99a64e10dfcf6608a1d47f4349676c745bf234cebd52826d786db9a3be2811"]["IPv4Address"])