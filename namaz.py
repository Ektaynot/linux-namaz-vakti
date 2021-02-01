import http.client
import os
import time
import datetime
import ast
import sys

logloc=os.path.expanduser('~/.cache/namaz/log.txt')
filevarmı=os.path.exists(logloc)
if filevarmı==False:
	os.system("mkdir -p ~/.cache/")
	os.system("mkdir -p ~/.cache/namaz/")
	os.system("touch ~/.cache/namaz/log.txt")

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey xxxxx"
    }

data=""

def vakit():
    conn.request("GET", "/pray/all?data.city=kocaeli", headers=headers)
    res = conn.getresponse()
    data = res.read()
    file2write=open(f"{yer}",'a')
    file2write.write(f'{(data.decode("utf-8"))}\n')
    file2write.close()
    print("oluşturuldu")

def hesap(farki,suan,kime,saatkaca):
    if farki<60:
        dakika=f'{farki} dakika'
    elif farki>60 and farki<120:
        dakika=f"1 saat {farki-60} dakika"
    elif farki>120 and farki<180:
        dakika=f"2 saat {farki-120} dakika"
    elif farki>180 and farki<240:
        dakika=f"3 saat {farki-180} dakika"
    elif farki>240 and farki<300:
        dakika=f"4 saat {farki-240} dakika"
    os.system(f"notify-send 'Şu An {suan}' '{kime} Saati:{saatkaca} | Kalan Süre {dakika}'")


x = datetime.datetime.now()
logloc2=os.path.expanduser(f'~/.cache/namaz/{x.strftime("%Y-%m-%d")}.txt')
def bildirim():
    with open(logloc2,"r") as data:
        users = data.read()
    imsak=(users[20:25])
    gunes=(users[53:58])
    ogle=(users[86:91])
    ikindi=(users[118:123])
    aksam=(users[152:157])
    yatsı=(users[185:190])
    now = datetime.datetime.now()
    saat=str(f'{now.hour}:{now.minute}').replace(" ", "")
    imsak2 = int(imsak[0:2])*60 + int(imsak[3:5])
    gunes2 = int(gunes[0:2])*60 + int(gunes[3:5])
    ogle2 = int(ogle[0:2])*60 + int(ogle[3:5])
    ikindi2 = int(ikindi[0:2])*60 + int(ikindi[3:5])
    aksam2 = int(aksam[0:2])*60 + int(aksam[3:5])
    yatsı2 = int(yatsı[0:2])*60 + int(yatsı[3:5])
    if saat[1]==":":
        saat="0"+saat
    zaman=int(saat[0:2])*60 + int(saat[3:5])

    if zaman < imsak2 or zaman>yatsı2:
        os.system(f"notify-send 'Şu An Yatsı' 'İmsak Saati:{imsak}'")
            
    elif zaman < ogle2 and zaman>imsak2:
        hesap(ogle2-zaman,"İmsak","Öğle",ogle)
        print("imsak")
    elif zaman < ikindi2 and zaman>ogle2:
        hesap(ikindi2-zaman,"Öğle","İkindi",ikindi)
        print("ogle")
    elif zaman < aksam2 and zaman>ikindi2:
        hesap(aksam2-zaman,"İkindi","Akşam",aksam)
    elif zaman < yatsı2 and zaman>aksam2:
        hesap(yatsı2-zaman,"Akşam","Yatsı",yatsı)
        print("aksam",saat)

if os.path.exists(logloc2) == False:
    yer=os.path.expanduser(f'~/.cache/namaz/{x.strftime("%Y-%m-%d")}.txt')
    os.system(f'touch ~/.cache/namaz/{x.strftime("%Y-%m-%d")}.txt')
    print("ol")
    vakit()
    bildirim()

elif os.path.exists(logloc2) == True:
    bildirim()
