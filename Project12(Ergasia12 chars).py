#ανηγμα του αρχειου
with open("test.txt")as f:
    data=f.read()
txt=data
print(txt)
i=len(txt)
print(i)
#μετατροπη του πρωτου γραμματος σε κατοπρικο
p=ord(txt[1])
k=128-p
ft=chr(k)
#επαναληπτικη διαδικασια για τους υπολλιπους
for x in range(len(txt)-1):
    p=ord(txt[x+1])
    k=128-p
    ft=chr(k)+ft
print(ft)
print(len(ft))
#αντιστροφη του κειμενου
fft=ft[::-1]
print(fft)
print(len(fft))
