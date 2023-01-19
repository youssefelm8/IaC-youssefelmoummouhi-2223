### Step 1: Define Python Data Rules

### REWRITING RULES TO GENERATE THE DATA STRUCTURE

###Most of the time you will have to manage structures of type dict and list, as a result of the JSON exhange data types

###member_dict   =  {"person_name": "x", "email": "y", "group":"z"}
###member_list   =  [member_dict]

###group_dict    =  {group_name, member_list} | {group_name, [member_dict]}  
###group_list    =  [group_dict]

###groups_struc  =  {group_list} | {[group_dict]}

### Step 2: Read Two Excel Records

### Simplified code: converting Excel into initial Python dict
import xlrd   # library to manage excel spreadsheets
import json   # library to manage JSON classes and functions

wb = xlrd.open_workbook("webex_groups.xlsx")
sheet = wb.sheet_by_index(0)  # read data from the first tab
member_dict = {}
member_dict["group"] = sheet.cell_value(1, 0)
member_dict["person_name"]  = sheet.cell_value(1, 1)
member_dict["email"] = sheet.cell_value(1, 2)

member_dict["group"] = sheet.cell_value(2, 0)
member_dict["person_name"]  = sheet.cell_value(2, 1)
member_dict["email"] = sheet.cell_value(2, 2)


### Step 3: Read All Excel Records

### Simplified code: converting all Excel data into initial Python dict

import xlrd   # library to manage excel spreadsheets
import json   # library to manage JSON classes and functions

def find_all_persons_and_groups(xlf):
    ### READ EXCEL FILE AND RETURN NUMBER OF ROWS
    wb = xlrd.open_workbook(xlf)
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    all_members = []
    for r in range(number_rows):
        if r > 0: ### first row contains columns names
            COL_A =  sheet.cell_value(r, 0)  #### column A
            COL_B =  sheet.cell_value(r, 1)  #### column B
            COL_C =  sheet.cell_value(r, 2)  #### column C
            member_dict["group"] = COL_A
            member_dict["person_name"]  = COL_B
            member_dict["email"] = COL_C
            all_members.append(member_dict.copy())    
    return all_members

###Function Call in Python Script:
member_list = find_all_persons_and_groups("webex_groups.xlsx")

### Step 4:  Tree Structure Level 1

### Simplified code: making list of groups from initial Python dict
def make_list_of_groups(membr_list):    
    all_groups = []
    mem = None
    for rec in membr_list:
        g = rec["group"]
        if mem != g:
            all_groups.append(g)
        mem = g
   
    return all_groups

group_list  = make_list_of_groups(member_list)  

for el in group_list:
    print (el)

### Step 5: Tree Structure Level 1 & 2

### Simplified code: attaching group members (L2) to their group (L1)
def attach_members_to_groups(group_name, membr_list):        
    membr_dict         = {}
    all_group_members  = [membr_dict]
    #print(loc_group)
    for membr in membr_list:
        if membr["group"] == group_name:
            #print(membr)
            if membr["person_name"] != None:
                membr_dict["person_name"]  = membr["person_name"]
                membr_dict["email"] = membr["email"]
                #print(loc_m_dict)
                all_group_members.append(membr_dict.copy())
    return all_group_members

       
 


### Step 6: main()

###  Simplified code: calling three functions + creating final data structure
###  It is necessary to have an Excel file
###  with the name"webex_groups.xlsx" or change the name)
def main():
    groups_struc = {}
    groups_struc ["groups"] = []
    member_list = find_all_persons_and_groups("webex_groups.xlsx")
    group_list  = make_list_of_groups(member_list)  
    all_members = []
    for group_rec in group_list:
        all_members = attach_members_to_groups(group_rec, member_list)
        del all_members[0] #### delete the first element, which is a copy of the last element
        group_dict = { "group": {"group_name": group_rec , "members": all_members }}
        groups_struc['groups'].append(group_dict) # updated 18JAN2022
    js_groups = json.dumps(groups_struc)
    print (js_groups)
   
#### execute main() when called directly        
if __name__ == '__main__':
    main()