kalin = ["a","ı","o","u"]
ince = ["e","i","ö","ü"]
kalin_test=[]
ince_test=[]

print("Kalin",kalin)
print("Ince ",kalin)
kelime = input("Kelime girin")

for i in range(0,len(kelime)):
    if(kelime[i]=="a"):
        kalin_test.append(kelime[i])
    elif(kelime[i]=="ı"):
        kalin_test.append(kelime[i])
    elif(kelime[i]=="o"):
        kalin_test.append(kelime[i])
    elif(kelime[i]=="u"):
        kalin_test.append(kelime[i])
    elif(kelime[i]=="e"):
        ince_test.append(kelime[i])
    elif(kelime[i]=="i"):
        ince_test.append(kelime[i])
    elif(kelime[i]=="ö"):
        ince_test.append(kelime[i])
    elif(kelime[i]=="ü"):
        ince_test.append(kelime[i])
if(len(kalin_test)>=1 and len(ince_test)<1):
    print("Buyuk unlu uyumuna uyuyor")
elif(len(kalin_test)<1 and len(ince_test)>=1):
    print("Büyük ünlü uyumuna uyuyor")
elif(len(kalin_test)>=1 and len(ince_test)>=1):
    print("Büyük ünlü uyumuna uymaz")
elif(len(kalin_test)<1 and len(ince_test)<1):
    print("Büyük ünlü uyumuna uymaz")