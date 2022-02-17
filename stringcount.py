def string_count(string):
    d = dict()
    for key in string:
        if key  in  d:
            d[key]+=1
        else:
            d[key]=1
    return d
string = 'MISSISSIPPI'
print (string_count(string))
