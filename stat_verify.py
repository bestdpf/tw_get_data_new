import io
import json
import os
import sys
verify_fr=0
verify_fl=0
all_fr=0
all_fl=0
verify_cnt=0
cnt=0
with open('succ.txt','r') as f:
    for line in f:
        if line == '\n':
            continue
        usr_id=int(line)
        #usr_id,dis=[int(x) for x in line.split()]
        if os.stat(str(usr_id)+'/user_info.json').st_size==0:
            continue
        usr_timeline_data=open(str(usr_id)+'/user_info.json')
        usr_timeline=json.load(usr_timeline_data)
        all_fr=all_fr+usr_timeline['friends_count']
        all_fl=all_fl+usr_timeline['followers_count']
        cnt=cnt+1
        #print usr_timeline['verified']
        if usr_timeline['verified'] :
            print '------------'
            verify_cnt=verify_cnt+1
            verify_fr=verify_fr+usr_timeline['friends_count']
            verify_fl=verify_fl+usr_timeline['followers_count']
print verify_fr
print verify_fl
print all_fr
print all_fl
