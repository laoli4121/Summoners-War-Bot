from qpyou import QPYOU
from api import API
from tools import Tools

uid,did=QPYOU('229313295').createNew()
a=API(uid,did)
a.setIDFA(Tools().rndDeviceId())
a.getServerStatus()
a.getVersionInfo()
a.CheckLoginBlock()
a.GuestLogin()
a.doMission(1,1,1)#garen forest outskirts
a.doMission(1,2,1)#garen forest south
a.doMission(1,3,1)#garen forest east
a.doMission(1,4,1)#garen forest paths