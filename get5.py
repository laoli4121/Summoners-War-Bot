from api import API
from qpyou import QPYOU
from tools import Tools
import time
from random import randint

mon_class=0
while(True):
	uid,did=QPYOU().createNew()
	a=API(uid,did)
	a.setRegion('sea')
	a.setIDFA(Tools().rndDeviceId())
	a.login()
	mon_class, mon_id = a.auto_run()
	if mon_class != 3:
		f = open("lightMonster.txt","a+")
		f.write("%s, %s: %s"%(mon_class,mon_id,uid))
	time.sleep(randint(120,300))
