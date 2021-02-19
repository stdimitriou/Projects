import random
print("give number of rows: ")
i=input()
print("give number of lines: ")
j=input()
i=int(i)
j=int(j)
pos=i*j
sos=[]
sos1=[]
x=0
half=int(pos/2)
for p in range(100):
    o=0
    s=0
    #filling up the "array"
    for k in range(i):
        sos1=[]
        for l in range(j):
            if s<half:
                sos1.append("S")
                s=s+1
                if len(sos1)==j:
                    break
            if o<half:
                sos1.append("O")
                o=o+1
                if len(sos1)==j:
                    break
        #shuffle to create the random factor
        random.shuffle(sos1)
        sos.append(sos1)
    #second shuffle for maximum randomnes in case the first one didnt change a lot
    random.shuffle(sos)
    #finding all the posible sos
    for k in range(i-2):
        for l in range(j-2):
            if sos[k][l]=="S" and sos[k][l+1]=="O" and sos[k][l+2]=="S":
                x=x+1
            if sos[k][l]=="S" and sos[k+1][l]=="O" and sos[k+2][l]=="S":
                x=x+1
            if sos[k][l]=="S" and sos[k+1][l+1]=="O" and sos[k+2][l+2]=="S":
                x=x+1
            if k==j-2:
                if sos[k+1][l]=="S" and sos[k+1][l+1]=="O" and sos[k+1][l+2]=="S":
                    x=x+1
                if sos[k+2][l]=="S" and sos[k+2][l+1]=="O" and sos[k+2][l+2]=="S":
                    x=x+1
#in case x=0 propable imposible
if x>0:
    print(x/100)
else :
    print("0 number of sos")
