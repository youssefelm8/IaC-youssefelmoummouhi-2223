import json
with open ('Workshop/RestCONF/data.json', 'r') as json_file:
    response_json = json.load (json_file)
    
print("=> Printing filtered response")
print("Interface Name: ")
if_name = response_json["ietf-interfaces:interfaces"]["interface"][0]["name"]
print(if_name)
print("IP Address + Subnet: " )
ip_subnet = response_json["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"] 
print(ip_subnet)
print("IP Address: " )
ip = response_json["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"][0]["ip"]
print(ip)