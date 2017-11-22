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