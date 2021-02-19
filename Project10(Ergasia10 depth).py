import json
def depth(dic):
    #counting the depth
    str_dic = str(dic)
    counter = -1
    for i in str_dic:
        if i == "{" or i=="[":
            counter += 1
    return(counter)
#opening file
with open("dc.txt")as f:
    data=f.read()
d=json.loads(data)
#finding the depth
print(d,"το βαθος ειναι :",depth(d))
