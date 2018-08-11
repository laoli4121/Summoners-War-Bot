from api import API
from qpyou import QPYOU
from tools import Tools
import time
from random import randint
import monster

mon_class=0
while(True):
	try:
		uid, did = QPYOU().createNew()
		a = API(uid, did)
		a.setRegion('sea')
		a.setIDFA(Tools().rndDeviceId())
		a.login()
		mon_class, mon_id = a.auto_run()
		if mon_class != 3:
			mon_name = monster.monsters_name_map[str(mon_id)[0:3]]
			f = open("lightMonster.txt", "a+")
			f.write("%s, %s:%s %s  --%s\n" % (mon_class, mon_id, mon_name, uid, time.strftime('%H:%M')))
			f.close()
		a.doDungeonAndSellRune(8001, 1)
		a.UpdateAchievement(a.makeList(203, 1, 1))
		a.doDungeonAndSellRune(8001, 2)
		a.doDungeonAndSellRune(8001, 3)
		a.doDungeonAndSellRune(8001, 4)
		a.UpdateAchievement(a.makeList(204, 1, 1))
		a.doDungeonAndSellRune(8001, 5)
		a.repeatDoDungeonAndSellRune(8001, 6)
		for i in range(10):
			a.log("summoning...")
			mon_class, mon_id = a.SummonLight(2)
			if mon_class == 5:
				mon_name = monster.monsters_name_map[str(mon_id)[0:3]]
				print("class: %s, mon_id:%s mon_name:%s"%(mon_class,mon_id,mon_name))
				f = open("lightMonster.txt", "a+")
				f.write("%s, %s:%s %s  --%s\n" % (mon_class, mon_id, mon_name, uid, time.strftime('%H:%M')))
				f.close()
	except:
		print("error! trying...")
	time.sleep(randint(30,60))
