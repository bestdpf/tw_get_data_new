#!/usr/bin/python
from twitter import *
from bitarray import *
import io
from shutil import *
import sys
import traceback
import time
import urllib
from urllib import *
import urllib2
import json
import oauth2
import base64
import httplib
import gzip
import os
from random import *
from collections import deque
keys=['RQdTKNgo1NmB6r3oum0HKg'
      ,'RKrh8lrDgUnAv1xm3q4Pg'
      ,'jMP4DpdBC38KxxsGOOGWw'
      ,'xMigmqyxPwcDbh3RvYWw'
      ,'W3cFcf1ZIaKHl05fHZD2GA'
      ,'FqqYQmlX0uS9cjb1HsVJjQ'
      ,'apyxdn50fQF4O5P4TmOXw'
      ,'3V8xjCrO8MxTi5rMoj3JZw'
      ,'47T4dnztSnTbXVlqdx6hzw'
      ,'uSvCPBsQGNWuJLZZ30oYBA'
      ,'sSP8jKLD1KpsNZEzxadbA'
      ,'xCxdEv7BWN6kiArsRqZaw'
      ,'65i0EALXM1JRcFZ0lU2w'
      ,'rEQtlWO1OXVP9voI2Q'
      ,'xr1iepy9iHoky8Irxaj1eg'
      ,'V9QTUTz5keNaWTDPwcepA'
      ,'nsUpEowtdGXL7fq6UfaQ7Q'
      ,'FlMwFuPZkmQ4LWgFdJAuw'
      ,'gVlK1vGayBmFCDQj2A2UTg'
      ,'wKXavs24my6y2jUxNq5s5Q'
      ,'qsAF2YBsIxhwrMMNmRQXsA'
      ,'BOAwVlMgFHFXtQJ0PqR43Q'
      ,'KVk0kXf5kGpwZjvcIbwbQ'
      ,'TXKyONhrghQJr0VjGovbRQ'
      ,'ZpwtVGeisEPKoc0gHgjmYQ'
      ,'ILzwbL1WXEyv2xfpLhGXjw'
      ,'NtyLH8HMgcTzlURdlchcQ'
      ,'IAinqzyLaFzGCIeYHAXK5w'
      ,'JoOvBPn5VKY4JWEcTpR6FQ'
      ,'kynFuQQW3zbecWCSLKgAcA'
      ,'NJtrQnZBseXjRfYjWxo4hg'
      ,'4S1EKKf8Fj2Bjcgo345ig'
      
  ]
secrets=['dvmQdTxGfS9HfusWiZxG4pcdmSWKETSjERjCnLNmk'
     ,'Nhx1ERVYbQ8m18e7AhXL15Se6MAR3i9LP015qOcM'
     ,'VYGPGeRhR3dXZBvokCMxMiLNIIMUflgelP5RdiOTsE'
     ,'W4TcsqLpom2CYtk8bNOLnSLPRZYxQxsPc8zaUoUD1g'
     ,'1XjUJIFIiVUyzYlsLFJTsZOrSvdImI7BlazXq3a2ik'
     ,'Zq1ktMWkE1a1orsLVMrmR0XcHDtEclcjHLVUaLaXqVU'
     ,'u9NRyfK3qeL0KM8dWR9hMQjKs6BpZVQmIcAyhL5wAI'
     ,'BfPTwOfaC0PIfW2PUKRaquKX8IMCX7A7jUruBQ0bc'
     ,'5mC4regsO99rmxyJLu8noIDx5Eoxrp3VXHoSihaiek'
     ,'hSv9pceJKxVrpcxKEQG7VlDqdaUqQJXIGMbnliFQYY'
     ,'0lWasznt1ZAdJjjEzhUkOrCp6sddX76BHG1m6FDg'
     ,'BMby3c4vHDTyrnUx5YxN2hTY3G6vJ40U1yxiYk2Tk'
     ,'ZSFqG0Y7GDXSUCTSEIGJtJnesVKuBPUIlpxQMJdcxA'
     ,'PsDhBpngmcci6QFoTDDKgoO7Hz3cg9KjcUo8fjD3c'
     ,'OHP5PjKMPZtRp2nPBDK7OqPPqkljWFKZbdb9IP1gA'
     ,'XXZcnj6aIwbb3IEV0Cs1s9sNB54xCMYQ6nt1sfgbaU'
     ,'VT7gLTb2IJEOm4ESYmmdOYjHPr442CAjafWM13EU'
     ,'OLQJRzqZWUDqbKTaSLQ0SVwCNpnmdI6x1pBAMI'
     ,'JfRabi2LUalOzKOQ2jfRXrVzlYXQsIexYgdWEb6pPE'
     ,'yA61tqyIRjXtc9YqaokB5u5EGHUe5sRMOuibdDhmbc'
     ,'naH0duJXCWq7AtdZGDu27GBQ5f7Ho0dkm1PdoqXWHD8'
     ,'YX26wrMNLEHz8I7oB2LiIUG3Hb1l9uicKcDM92C8'
     ,'bpOsdk4koSpNaMLspHUHd4UdyOP3VEc2gazZ3u2c6c'
     ,'n1uoWQQzgcRZwhCgayfQWegfMUgqyf9Fh2cld82FAU'
     ,'Ux2XHVG09m2wU9mF58K31XSe1JcvpCATio5WLW6eo'
     ,'YMsErq0Qv1aB7AsfNlq0SBcyeLZmZKIuvt7nVYlY9xg'
     ,'P3WrvEjzpEhO3T6rC9nMSm1lgYnGEbIHng5pTydl8XI'
     ,'4191YKYAX80fYTEi8UDatViQWIF6Rum89puu7K8B5A'
     ,'jO39mH0S4LLBAR7HjZF6aoi6JbBKsx5NllYRJPB5G78'
     ,'d8Qvn9HWRt9XMP7IHcn3OjRlpoxjZS36TehAexiqY'
     ,'c9Yz97qtzFhKcOUtf9genXRJVKqGSaShAB6nidB6d8'
     ,'H234hsJlxYOS2C6tE9nLc1mzGI4KI6Fb5OIE4h9Y7c'
  ]

def get_token(consumer_key,consumer_secret):
    encoded_CONSUMER_KEY = urllib.quote(consumer_key)
    encoded_CONSUMER_SECRET = urllib.quote(consumer_secret)

    concat_consumer_url = encoded_CONSUMER_KEY + ":" + encoded_CONSUMER_SECRET

    host = 'api.twitter.com'
    url = 'https://api.twitter.com/oauth2/token/'
    params = urllib.urlencode({'grant_type' : 'client_credentials'})
    #req = httplib.HTTPSConnection(host)
    headers={"POST": url
    ,"Host": host
    ,"User-Agent": "My Twitter 1.1"
    ,"Authorization": "Basic %s" % base64.b64encode(concat_consumer_url)
    ,"Content-Type" :"application/x-www-form-urlencoded;charset=UTF-8"
    ,"Content-Length": "29"
    }
    req=urllib2.Request(url,params,headers)
    resp=urllib2.urlopen(req)
    data=json.load(resp)
    return data['access_token']
#step 1: auth
"""
t=Twitter(
        auth=OAuth('154578459-r47GrYDK2LpAjjyvyKLTz9fb2p1mkiYQXp7xmyrK'
        ,'8P4mS3MIdJCFYCcmbRzYciLYxtxXaMoCRNdkCp0GeA'
        ,'RQdTKNgo1NmB6r3oum0HKg'
        ,'dvmQdTxGfS9HfusWiZxG4pcdmSWKETSjERjCnLNmk'))
"""
tws=[]
len_of_keys=len(keys)
for i in range(0,len_of_keys):
    print 'launch tws {0}'.format(i)
    tmpt=Twitter(
        auth=OAuth2(bearer_token=get_token(consumer_key=keys[i],consumer_secret=secrets[i]))
    )
    tws.append(tmpt)
#print t.application.rate_limit_status()
#sys.exit()
abit=bitarray(10000000)
def get_mod(num):
    return num%10000000

class tw_ref:
    def __init__(self, obj): self.obj = obj
    def get(self):    return self.obj
    def set(self, obj):      self.obj = obj

pt=randint(0,len_of_keys-1)
t=tw_ref(tws[pt])
f_cnt=0
last_succ_id=154578451
qu=deque()
def get_data(idx):
    #qu=deque()
    qu.appendleft(idx)
    while qu:
        it=qu.popleft()
        if(abit[get_mod(it)]):
            print '{0} is skip for hash hitting'.format(it)
        else:
            print 'get {0} \'s info'.format(it)
            abit[get_mod(it)]=True
            if not os.path.exists(str(it)):
                os.mkdir(str(it))
            f_fr=open(str(it)+'/friends.json','w')
            f_fl=open(str(it)+'/followers.json','w')
            f_ui=open(str(it)+'/user_info.json','w')
            f_tl=open(str(it)+'/user_timeline.json','w')        
            try:
                friends=t.get().friends.ids(user_id=it);
                #f_fr=io.open(str(it)+'/friends.json','wb')
                #f_fr.write(str(friends))
                json.dump(friends,f_fr)
                f_fr.close()
                followers=t.get().followers.ids(user_id=it);
                #f_fl=io.open(str(it)+'/followers.json','wb')
                #f_fl.write(str(followers))
                json.dump(followers,f_fl)
                f_fl.close()
                user_info=t.get().users.show(user_id=it)
                #f_ui=io.open(str(it)+'/user_info.json','wb')
                #f_ui.write(str(user_info))
                json.dump(user_info,f_ui)
                f_ui.close()
                timeline=t.get().statuses.user_timeline(user_id=it)
                #f_tl=io.open(str(it)+'/user_timeline.json','wb')
                #f_tl.write(str(timeline))
                json.dump(timeline,f_tl)
                f_tl.close()
                global last_succ_id
                last_succ_id=it
                f_succ=io.open('succ.txt','ab')
                f_succ.write(str(it)+'\n')
                f_succ.close()
            except  TwitterHTTPError as err:
                print 'Error code {1} get when get {0} info'.format(it,err.e.code)
                if err.e.code==429:
                    f_extends_err=io.open('extends.txt','ab')
                    f_extends_err.write(str(it)+'\n')
                    f_extends_err.close()
                    qu.append(it)
                    global pt
                    tmppt=(pt+1)%len_of_keys
                    pt=tmppt
                    print 'change twitter client to tws {0}'.format(pt)
                    #print 'Sleeping 15mins now for Rate Limiting'
                    time.sleep(5)
                    t.set(tws[pt])
                    #get_data(it)
                if os.listdir(str(it)) == []:
                    rmtree(str(it))
                #traceback.print_exc(file=sys.stdout)
                #cannot get data for privacy protection
                if err.e.code==401:
                    f_http_err=io.open('http_err_id.txt','ab')
                    f_http_err.write(str(it)+'\n')
                    f_http_err.close()
            except  Exception:
                print 'get other exception '
                global f_cnt
                f_cnt=f_cnt+1
                print 'write fail'
                f_fail=io.open('fail.txt','wb')
                f_fail.write(str(it)+'\n')
                f_fail.close()
                print 'write last_succ'
                f_last_succ=io.open('last_succ.txt','wb')
                f_last_succ.write(str(last_succ_id)+'\n')
                f_last_succ.close()
                qu.append(it)
                pt=(pt+1)%len_of_keys
                t.set(tws[pt])
                print 'change to tws {0}'.format(pt)
                time.sleep(5)
                traceback.print_exc(file=sys.stdout)
                if f_cnt > 5:
                    print 'restart now ...'
                    sys.exit()
            finally:
                f_fr.close()
                f_tl.close()
                f_ui.close()
                f_fl.close()

abit.setall(False)
with io.open('succ.txt','r') as f:
    for line in f:
        #print get_mod(int(line))
        abit[get_mod(int(line))]=True
with io.open('http_err_id.txt','r') as f:
    for line in f:
        abit[get_mod(int(line))]=True
#change the id_it to some other to get some set of new data
#id_it=154578451
id_it=int(sys.argv[1])
print 'starting with {0} now'.format(id_it)
if id_it == []:
    id_it=154578451
#qu.append(id_it)
abit[get_mod(id_it)]=False
with io.open('extends.txt','r') as f:
    for line in f:
        qu.append(int(line))
with io.open('fail.txt','r') as f:
	for line in f:
		qu.append(int(line))
get_data(id_it)
print 'done of all the failuer data'
