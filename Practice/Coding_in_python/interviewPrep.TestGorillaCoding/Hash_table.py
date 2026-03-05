import ast
import json
def print_hash_table(sublists):
    #better way to convert to sublists
    sublists_udt = ast.literal_eval(sublists)
    table = { }
    for sublist in sublists_udt:
        if sublist != []:
            for sub in sublist:
                table[sub[0]] = sub[1]
    #to return it as with double quotes, not single quotes: {"Day": "Monday", "Forum": "Celaya", "Device": "Smartphone"}
    return json.dumps(table)

sublists = input()
print(print_hash_table(sublists))

