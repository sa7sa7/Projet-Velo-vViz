import urllib3
from time import sleep
http = urllib3.PoolManager()
i = 106;
while(1):
    r = http.request('GET', 'https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json')
    i = i +1 
    name = "file"+str(i)
    f= open(name+".json","wb")
    f.write(r.data)
    f.close() 
    sleep(300)