curl -i -k \
-X "PUT" "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface=$LOOPBACK_INTERFACE" \
-H "Accept: application/yang-data+json" \
-H "Content-type: application/yang-data+json" \
-u 'developer:C1sco12345' \
-d $'{
  "ietf-interfaces:interface": {
     "name": "Loopback199",
     "description": "RESTCONF => Loopback199",
     "type": "iana-if-type:softwareLoopback",
     "enabled": "true",
     "ietf-ip:ipv4": {
         "address": [
             {
                 "ip": "10.1.99.1",
                 "netmask": "255.255.255.0"
             }
         ]
     }
 }
}' 


