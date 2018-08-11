from api import API
from qpyou import QPYOU
from tools import Tools



my_email='smwpython+014@gmail.com'
my_hivelogin='smw00014'
my_password='smw12345'

uid,did,sessionkey=QPYOU('542057052').hiveLogin(my_hivelogin,my_password) #mydid
a=API(uid,did,my_hivelogin,my_email,sessionkey)
a.setRegion('sea')
a.setIDFA(Tools().rndDeviceId())
a.getServerStatus()
a.getVersionInfo()
a.CheckLoginBlock()
a.login()

# a.completeDaily()
a.repeatDoDungeonAndSellRune(8001,9)

# a.setCanArena()
# a.completeDaily()
# a.completeTutorial()
# a.completeDaily()
# a.completeRegion(9,1,5)
# a.level8()
# a.level2()
# a.level3()
# a.completeTower(2,81)#Start from 82
# a.doDungeonAndSellRune('9001','10')#Dragon stage 10
# a.doRiftDungeonAndSellRune(5001)#Start rift water
# a.completeDaily()
# a.powerUpRune(11195338165,5,9)
# a.setCanArena()
# a.repeatDoDungeonAndSellRune(9001,10)
# a.repeatDoRiftDungeonAndSellRune(2001)
# a.growUp()
# a.completeTutorial()
# a.completeAchivment()
# a.doMission(1,1,1)#garen forest outskirts
# a.doMission(1,2,1)#garen forest south
# a.doMission(1,3,1)#garen forest east
# a.doMission(1,4,1)#garen forest paths
