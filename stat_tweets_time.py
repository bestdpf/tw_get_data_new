import io
import json
import os
import sys
#time_container=[0]*60*24
month_container=[0]*12*8
mk=dict()
mk['Oct']=10
mk['Jan']=1
mk['Nov']=11
mk['Dec']=12
mk['Sep']=9
mk['Aug']=8
mk['Jul']=7
mk['Jun']=6
mk['May']=5
mk['Apr']=4
mk['Mar']=3
mk['Feb']=2
with open('succ.txt','r') as f:
    for line in f:
        if line == '\n':
            continue
        usr_id=int(line)
        #usr_id,dis=[int(x) for x in line.split()]
        if os.stat(str(usr_id)+'/user_timeline.json').st_size==0:
            continue
        usr_timeline_data=open(str(usr_id)+'/user_timeline.json')
        usr_timeline=json.load(usr_timeline_data)
        for tweet in usr_timeline:
            #print tweet
            week,month,date,time,time_zone,yr=[x for x in tweet['created_at'].split()]
            hour,minute,second=[int(x) for x in time.split(':')]
            #total_time=hour*60+minute
            #print month
            total_month=(int(yr)-2006)*12+mk[month]-1
            #print total_time
            #time_container[total_time]=time_container[total_time]+1
            month_container[total_month]=month_container[total_month]+1
f_succ=open('succ_month_stat.txt','w')
f_succ.write('[')
for i in range(0,12*8-2):
    f_succ.write(str(month_container[i])+',')
f_succ.write(str(month_container[12*8-1])+'];')
f_succ.close()
