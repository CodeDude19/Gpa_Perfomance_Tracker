import os
list_of_files = os.listdir("C:\\Users\\Yasser Arafat\\Desktop\\all_subject_dump")

##########################################################################################

n = len(list_of_files)

##########################################################################################

import json
list = [] # this is a list containing all the json data of each subject listed against their subject name!
for i in range(n):
    file = open("C:\\Users\\Yasser Arafat\\Desktop\\all_subject_dump\\{}".format(list_of_files[i]),"r")
    list.append(json.load(file))

##########################################################################################

list_of_reg = []
for i in range(n):
    for key,value in list[i].items():
        if key not in list_of_reg:
            list_of_reg.append(key)

##########################################################################################

n1 = len(list_of_reg)
dict_large = {}
for j in range(n1):
    dict_small = {"{}".format(list_of_reg[j]):{}}
    for k in range(n):
        if list_of_reg[j] in list[k]:
            dict_small[list_of_reg[j]].update(list[k][list_of_reg[j]])
    dict_large.update(dict_small)
new_file = open("C:\\Users\\Yasser Arafat\\Desktop\\new_dump.json","w")
json.dump(dict_large,new_file)
new_file.close()
