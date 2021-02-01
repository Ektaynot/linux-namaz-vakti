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
    'authorization': "apikey xxxxxxx"
    }

data=""

def vakit():
    conn.request("GET", "/pray/all?data.city=istanbul", headers=headers)
    res = conn.getresponse()
    data = res.read()
    file2write=open(f"{yer}",'a')
    file2write.write(f'{(data.decode("utf-8"))}\n')
    file2write.close()
    print("oluşturuldu")

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
    zaman=int(saat[0:2])*60 + int(saat[3:5])
    if zaman < imsak2 or zaman>yatsı2:
        os.system(f"notify-send 'Şu An Yatsı' 'İmsak Saati:{imsak}'")
        print("yatsı")
    elif zaman < gunes2 and zaman>imsak2:
        os.system(f"notify-send 'Şu An İmsak' 'Güneş Saati:{gunes}'")
        print("imsak")
    elif zaman < ogle2 and zaman>gunes2:
        os.system(f"notify-send 'Şu An Ogle' 'İkindi Saati:{ikindi}'")
        print("ogle")
    elif zaman < ikindi2 and zaman>ogle2:
        os.system(f"notify-send 'Şu An İkindi' 'Akşam Saati:{aksam}'")
        print("ikindi")
    elif zaman < yatsı2 and zaman>ikindi2:
        os.system(f"notify-send 'Şu An Akşam' 'Yatsı Saati:{yatsı}'")
        print("aksam")

if os.path.exists(logloc2) == False:
    yer=os.path.expanduser(f'~/.cache/namaz/{x.strftime("%Y-%m-%d")}.txt')
    os.system(f'touch ~/.cache/namaz/{x.strftime("%Y-%m-%d")}.txt')
    vakit()
    bildirim()

elif os.path.exists(logloc2) == True:
    bildirim()
