### JSON FILTERING -- SERVICES DATA

import json

servers_struc = {
 "rack": [
      { "server": { "dev_id": "S1" , "server_name": "svr1" , "domain": "biasc.be", "ip-address": "10.2.3.11" ,
                     "os": "linux"  , "server_type": "vm" ,
                     "services": [  
                       {"service": "ad" , "service_type": "vm", "protocol": "tcp", "port": "389"},
                       {"service": "dns", "service_type": "vm", "protocol": "udp", "port": "53"},
                       {"service": "ntp", "service_type": "vm", "protocol": "udp", "port": "123"}
                    ]
                  }
      },
      { "server": { "dev_id": "S2" , "server_name": "svr2" , "domain": "biasc.be", "ip-address": "10.2.3.12" ,
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [  
                      {"service": "flask", "service_type": "vm", "protocol": "tcp", "port": "8089"  },
                      {"service": "db"   , "service_type": "vm", "protocol": "tcp", "port": "1521"  }
                    ]    
                 }
      },
      { "server": { "dev_id": "S3" , "server_name": "svr3" ,  "domain": "biasc.be" , "ip-address": "10.2.3.13",
                    "os": "linux"  , "server_type": "vm" ,
                    "services": [  
                      {"service": "dns" , "service_type": "vm", "protocol": "tcp", "port": "8089" },
                      {"service": "ntp" , "service_type": "vm", "protocol": "udp", "port": "123" },
                      {"service": "dhcp", "service_type": "docker", "protocol": "udp", "port": "67" }
                    ]
                  }
      }
   ]
}

print('------1---------')
print(type(servers_struc))
print(servers_struc)
print('------1A--------')
js_groups = json.dumps(servers_struc)
print(type(js_groups))
print(js_groups)
print('------1B--------')
print(json.dumps(servers_struc, indent=2))

print('------2---------')
for g in servers_struc["rack"]:
    print('------2A--------')
    print(type(g))
    print(g)
    print(g["server"]["services"])
    for p in g["server"]["services"]:
        print(p)
           
print('------3---------')
print(servers_struc.keys())

print('------3A---------')
print(servers_struc["rack"][0].keys())

print('------3B---------')
print(servers_struc["rack"][0]["server"]["ip-address"])

print('------3C---------')
print(servers_struc["rack"][-1]["server"]["services"][1]["port"])

print('------3D---------')
for s in servers_struc["rack"]:
    print (s["server"]["server_name"] + " | " +s["server"]["ip-address"])

print('------3E---------')
for s in (servers_struc ["rack"][-1]["server"]["services"]):
    print(s["port"])