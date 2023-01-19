import json
with open ('Workshop/Webex API Response Data/data.json', 'r') as json_file:
    response_json = json.load (json_file)
#DISPLAY FILTERED RESULTS 
print("Displaying partial information")
#print(type(res))
print("Name: " + response_json['displayName'])
print("id: " + response_json['id'])
print("Created: " + response_json['created'])
print("User Type: " + response_json['type'])
print("User Status: " + response_json['status'])