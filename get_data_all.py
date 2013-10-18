#!/usr/bin/python
from twitter import *
from os import *
from bitarray import *
import io
from shutil import *
import sys
import traceback
import time
#step 1: auth
t=Twitter(
        auth=OAuth('154578459-r47GrYDK2LpAjjyvyKLTz9fb2p1mkiYQXp7xmyrK'
        ,'8P4mS3MIdJCFYCcmbRzYciLYxtxXaMoCRNdkCp0GeA'
        ,'RQdTKNgo1NmB6r3oum0HKg'
        ,'dvmQdTxGfS9HfusWiZxG4pcdmSWKETSjERjCnLNmk'))
print t.application.rate_limit_status()
sys.exit()
abit=bitarray(10000000)

def get_mod(num):
    return num%10000000

def get_data(idx):
    if(abit[get_mod(idx)]):
        print '{0} is skip for hash hitting'.format(idx)
    else:
        print 'get {0} \'s info'.format(idx)
        abit[get_mod(idx)]=True
        if not path.exists(str(idx)):
			mkdir(str(idx))
        try:
			friends=t.friends.ids(user_id=idx);
			f_fr=io.open(str(idx)+'/friends.json','wb')
			f_fr.write(str(friends))
			followers=t.followers.ids(user_id=idx);
			f_fl=io.open(str(idx)+'/followers.json','wb')
			f_fl.write(str(followers))
			user_info=t.users.show(user_id=idx)
			f_ui=io.open(str(idx)+'/user_info.json','wb')
			f_ui.write(str(user_info))
			timeline=t.statuses.user_timeline(user_id=idx)
			f_tl=io.open(str(idx)+'/user_timeline.json','wb')
			f_tl.write(str(timeline))
			for i in friends['ids']:
				get_data(i)
			for i in followers['ids']:
				get_data(i)
        except  TwitterHTTPError as err:
			print 'Error code{1} get when get {0} info'.format(idx,err.e.code)
			if err.e.code==429:
				print 'Sleeping 15mins now for Rate Limiting'
				time.sleep(15*61)
			if os.listdir(str(idx))==[]:
				rmtree(str(idx))
			traceback.print_exc(file=sys.stdout)

abit.setall(False)
#change the id_it to some other to get some set of new data
id_it=154578451
get_data(id_it)


