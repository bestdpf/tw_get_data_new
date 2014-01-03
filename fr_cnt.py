import io
import json
import os
import sys
from random import *
from pprint import pprint
fr_cnt=[0]*10005
#fl_cnt=[0]*10005
#f_fr=open('fr_ids.txt','w')
#f_fl=open('fl_ids.txt','w')
f_fr_cnt=open('fr_cnt.txt','w')
f_fr_test=open('fr_2001.txt','w')
with open('succ.txt','r') as f:
    for line in f:
        #print line
        if line == '\n':
            continue
        usr_id=int(line)
        if os.stat(str(usr_id)+'/user_info.json').st_size==0 | os.stat(str(usr_id)+'/friends.json').st_size==0 |os.stat(str(usr_id)+'/followers.json').st_size==0  :
            continue
        usr_info_data=open(str(usr_id)+'/user_info.json')
        usr_info=json.load(usr_info_data)
        #usr_friends_data=open(str(usr_id)+'/friends.json')
        #usr_friends=json.load(usr_friends_data)
        #usr_followers_data=open(str(usr_id)+'/followers.json')
        #usr_followers=json.load(usr_followers_data)
        #print 'friends_count {0}\n'.format(usr_info['friends_count'])
        tfr_cnt=usr_info['friends_count']
        #tfl_cnt=usr_info['followers_count']
        if tfr_cnt >100000:
            continue
        #print tfr_cnt
        if tfr_cnt%10000==2001:
            f_fr_test.write('{0} {1}\n'.format(usr_id,tfr_cnt))
        fr_cnt[tfr_cnt%10000]=fr_cnt[tfr_cnt%10000]+1
        usr_info_data.close()
for i in range(0,10000):
    print '{0} {1}\n'.format(i,fr_cnt[i])
    f_fr_cnt.write('{0} {1}\n'.format(i,fr_cnt[i]))
f_fr_test.close()
