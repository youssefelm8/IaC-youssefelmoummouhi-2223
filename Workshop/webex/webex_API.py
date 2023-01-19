### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started ### (login required)

current_access_token = "MGRlMDY3MjctMmQxYy00MDEzLWJjMTUtMTcxNGRmMGZkMTQ1N2Y4NWM3ZWEtODFm_P0A1_252c1395-1f33-4afe-85cf-58b2de7a3ff4" ### add your own bearer token

### ADD NEW SPACES AND MEMBERS TO WEBEX TEAMS
### THIS CODE ONLY WORKS IF YOU ARE ABLE TO GENERATE A CORRECT GROUPS_STRUC

import requests
import json

from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token = current_access_token)

print("Creating spaces +  members --> from Excel spreadsheet in the previous cell")
access_token = current_access_token


### Two alternative main functions have been created
### main2() => RESTFUL API
### main()  => WEBEXTEAMSSDK


def main2(): # using rest api
    with open('groups_struc.json') as json_file:
       json_groups_struc = json_file.read()
    groups_struc = json.loads(json_groups_struc)

    url = 'https://api.ciscospark.com/v1/rooms'

    headers = { 'Authorization': 'Bearer {}'.format(access_token),
                'Content-Type': 'application/json' }



    for rec in groups_struc["groups"]:

        create_group_name = rec["group"]["group_name"]

        payload_space = {"title": create_group_name}

        if payload_space["title"] != None:  ### avoid errors if room title unknown

            res_space = requests.post(url, headers=headers, json=payload_space)
 
            if res_space.status_code < 300:

                NEW_SPACE_ID = res_space.json()["id"]
 
                for mbr in rec["group"]["members"]:

                    room_id = NEW_SPACE_ID

                    person_email = mbr["email"]

                    url2 = 'https://api.ciscospark.com/v1/memberships'

                    payload_member = {'roomId': room_id, 'personEmail': person_email}

                    res_member = requests.post(url2, headers=headers, json=payload_member)





#### execute main() when called directly        

if __name__ == "__main__":
    main2() ### or main()