def item_type(datalist):

    for item in datalist:
        print("item: ", item, " its Type is:  ", type(item), "\n")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
result = item_type(datalist)
