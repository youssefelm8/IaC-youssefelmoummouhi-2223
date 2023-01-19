#IMAGE
import json
f = open ("image_inspect.json", "r")
input_data = f.read()
#print (input_data)
docker_dict = json.loads(input_data)
print(docker_dict[0].keys())
print("------IMAGE------")
print(docker_dict[0]["RepoTags"])
print(docker_dict[0]["Created"])
print(docker_dict [0]["ContainerConfig"] ["Hostname"])
print(docker_dict[0]["DockerVersion"])




#CONTAINER
import json
f = open ("container_inspect.json", "r")
input_data = f.read()
#print (input_data)
docker_dict = json.loads(input_data)
print(docker_dict[0].keys())
print("------CONTAINER------")
print(docker_dict [0]["Config"] ["Hostname"])
print(docker_dict [0]["NetworkSettings"] ["Networks"] ["bridge"] ["IPAddress"]) 
print(docker_dict [0]["NetworkSettings"] ["Ports"])
print(docker_dict [0]["State"] ["Status"])