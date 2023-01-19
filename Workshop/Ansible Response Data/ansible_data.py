import json
with open ('Workshop/Ansible Response Data/data.json', 'r') as json_file:
    ansible_dict = json.load (json_file)
    
# PARSING AND FILTERING ANSIBLE JSON DATA 
print("---------1--------")
print("Showing dictionary keys at level 1")
#ansible_dict = json.loads(ansible_json_doc)
print(ansible_dict.keys())

print("---------2--------")
print("Showing keys of ansible facts at level 2")
print(ansible_dict['ansible_facts'].keys())

print("---------3--------")
print("Showing data below ansible facts: ip address")
print("IP Address: " + ansible_dict["ansible_facts"]["ansible_default_ipv4"]["address"])

print('---------4--------')
print("Showing data below ansible facts: ansible distribution")
print("Ansible Distribution: "  + ansible_dict["ansible_facts"]["ansible_distribution"])
print("Ansible Distribution Major: "  +ansible_dict["ansible_facts"]["ansible_distribution_major_version"])
print("Ansible Distribution Release: "  +ansible_dict["ansible_facts"]["ansible_distribution_release"])
print("Ansible Distribution Version: "  +ansible_dict["ansible_facts"]["ansible_distribution_version"])

print('---------5--------')
print("Showing data below ansible facts: kernel, nodename, os")
print("Ansible Kernel: "  +ansible_dict["ansible_facts"]["ansible_kernel"])
print("Ansible Nodename: "     + ansible_dict["ansible_facts"]["ansible_nodename"])
print("Ansible OS Family: "    + ansible_dict["ansible_facts"]["ansible_os_family"])
print("Ansible PKG Manager: "  + ansible_dict["ansible_facts"]["ansible_pkg_mgr"])
print("Ansible Python Version: "  + ansible_dict["ansible_facts"]["ansible_python_version"])

print('---------6--------')
print("Showing data below ansible facts: ansible environment")
print("Ansible Home: "  + ansible_dict["ansible_facts"]["ansible_env"]["HOME"])
print("Ansible User: "  + ansible_dict["ansible_facts"]["ansible_env"]["USER"])