from api import API
from qpyou import QPYOU
from tools import Tools

uid,did,sessionkey=QPYOU('236145028').hiveLogin('mila432f','hallo123')
a=API(uid,did,'mila432f','s@mila432.com',sessionkey)
a.setIDFA(Tools().rndDeviceId())
a.getServerStatus()
a.getVersionInfo()
a.CheckLoginBlock()
a.login()
#a.doMission(1,1,1)#garen forest outskirts
#a.doMission(1,2,1)#garen forest south
#a.doMission(1,3,1)#garen forest east
#a.doMission(1,4,1)#garen forest paths