input_dictionary = {
    "role_wise_permissions" : [
        {
            "roleName": "superadmin",
            "permissions": [
                {
                    "permissionName" : "profile",
                    "canView" : True,
                    "canAdd" : False,
                    "canEdit" : True,
                    "canDelete" : False,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": True
                },
                {
                    "permissionName" : "tags",
                    "canView" : True,
                    "canAdd" : True,
                    "canEdit" : True,
                    "canDelete" : True,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": False
                }
            ],
            "status": True
        },
        {
            "roleName": "user",
            "permissions": [
                {
                    "permissionName" : "profile",
                    "canView" : True,
                    "canAdd" : False,
                    "canEdit" : True,
                    "canDelete" : False,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": True
                },
                {
                    "permissionName" : "tags",
                    "canView" : True,
                    "canAdd" : True,
                    "canEdit" : True,
                    "canDelete" : True,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": True
                }
            ] ,
            "status": True
        },
        {
            "roleName": "operator",
            "permissions": [
                {
                    "permissionName" : "profile",
                    "canView" : True,
                    "canAdd" : False,
                    "canEdit" : True,
                    "canDelete" : False,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": True
                },
                {
                    "permissionName" : "tags",
                    "canView" : True,
                    "canAdd" : True,
                    "canEdit" : True,
                    "canDelete" : True,
                    "canUpload" : False,
                    "canDownload" : False,
                    "status": True
                }
            ] ,
            "status": False
        }
    ]
}

# Output should be:
# output_dictionary = {
#      "profile": {
#          "canView" : ["superadmin", "user"],
#          "canAdd" : [],
#          "canEdit" : ["superadmin", "user"],
#          "canDelete" : [],
#          "canUpload" : [],
#          "canDownload" : []
#      },
#      "tags": {
#          "canView" : ["user"],
#          "canAdd" : ["user"],
#          "canEdit" : ["user"],
#          "canDelete" : ["user"],
#          "canUpload" : [],
#          "canDownload" : []
#      }
#  }


def mainFunction(final_indata):
    output_dictionary = {}  # Creating a blank dictionary
    for item in final_indata['role_wise_permissions']:
        #print(item['status']) 
        if item['status']: # Checking status if it is true or false, superadmin, user are true, operator status is false
            for child in item['permissions']:
                # print(child['status'])
                if child['status']: # Permissions child checking status true or false. Output is True, False, True, True
                    # print(child['permissionName']) # profile, profile, tags
                    # print(output_dictionary) # {}
                    if child['permissionName'] not in output_dictionary:
                        # Using Hashmaps to create blank array
                        output_dictionary[child['permissionName']] = {
                            'canView': [],
                            'canAdd': [],
                            'canEdit': [],
                            'canDelete': [],
                            'canUpload': [],
                            'canDownload': []
                        }
                    # print(child['canView']) # True, True, True
                    # print(child['canAdd']) # False, False, True
                    # print(child['canEdit']) # True, True, True
                    # print(child['canDelete']) # False, False, True
                    # print(child['canUpload']) # False, False, False
                    # print(child['canDownload']) # False, False, False

                    # Appending data based on condition
                    permissionVar = output_dictionary[child['permissionName']]
                    if child['canView']:
                        # output_dictionary[child['permissionName']]['canView'].append(item['roleName'])
                        permissionVar['canView'].append(item['roleName'])
                    if child['canAdd']:
                        # output_dictionary[child['permissionName']]['canAdd'].append(item['roleName'])
                        permissionVar['canAdd'].append(item['roleName'])
                    if child['canEdit']:
                        # output_dictionary[child['permissionName']]['canEdit'].append(item['roleName'])
                        permissionVar['canEdit'].append(item['roleName'])
                    if child['canDelete']:
                        # output_dictionary[child['permissionName']]['canDelete'].append(item['roleName'])
                        permissionVar['canDelete'].append(item['roleName'])
                    if child['canUpload']:
                        # output_dictionary[child['permissionName']]['canUpload'].append(item['roleName'])
                        permissionVar['canUpload'].append(item['roleName'])
                    if child['canDownload']:
                        # output_dictionary[child['permissionName']]['canDownload'].append(item['roleName'])
                        permissionVar['canDownload'].append(item['roleName'])
                    
    print(output_dictionary)

mainFunction(input_dictionary)