#### DNA Center => Manage Enterprise Networks and Devices
#STEP 1 => DEFINE HARD CODED VARIABLES TO BE USED IN THE SCRIPT
####### TASKS
# TASK1: display the keys of the json repsonse
# TASK2: filter => hostname, type, ip address
# TASK3: display filtered data in a table format
import requests
import json
requests.packages.urllib3.disable_warnings()
print('Starting DNA Center Hello World - Simple')
print('Creating Hard Coded Variables')
# HARD CODED VARIABLES
DNAC_scheme = 'https://'
DNAC_authority='sandboxdnac2.cisco.com'
DNAC_port=':443'
DNAC_path_token='/dna/system/api/v1/auth/token'
DNAC_path='/dna/intent/api/v1/network-device'
DNAC_user = 'devnetuser'
DNAC_psw = 'Cisco123!'
#DNAC_user = input("Username? ")
#DNAC_psw = input("Password? ")
#STEP 2 => REQUEST TOKEN BASED ON USERNAME AND PASSWORD
print('Post First Request - Token')
# FIRST REQUEST
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
print(token_req_url)
auth = (DNAC_user, DNAC_psw)
print(type(auth))
req = requests.request('POST', token_req_url, auth=auth, verify=False)
#req = requests.request('POST', token_req_url, auth=(DNAC_user, DNAC_psw), verify=False)
#req = requests.post(token_req_url, auth=(DNAC_user, DNAC_psw), verify=False)
print(req)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
print(resp)
token = req.json()['Token']
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))