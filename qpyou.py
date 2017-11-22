import requests
import json
from tools import Tools
import random

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class QPYOU(object):
	def __init__(self):
		self.s=requests.session()
		self.s.verify=False
		self.s.headers.update({'Content-Type':'application/json','Accept-Language':'en-gb','User-Agent':'SMON_Kr/3.7.0.37000 CFNetwork/808.2.16 Darwin/16.3.0'})
		self.guest_uid=None
		self.p1='{"language":"en","timezone":null,"game_language":"en","server_id":"","device_country":"RU","hive_country":"RU"}'
		self.p2='{"hive_country":"RU","device_country":"RU","guest_uid":"%s","timezone":null,"language":"en","game_language":"en","server_id":""}'
		
	def create(self):
		res = json.loads(self.s.post('https://api.qpyou.cn/guest/create',data=self.p1).content)
		self.guest_uid=res['guest_uid']
		return res
	
	def auth(self):
		return json.loads(self.s.post('https://api.qpyou.cn/guest/auth',data=self.p2%(self.guest_uid)).content)
		
	def registered(self):
		return json.loads(self.s.post('https://api.qpyou.cn/device/registered',data=self.p1).content)
		
	def createNew(self):
		self.s.cookies.update({'advertising_id':Tools().rndDeviceId(),'appid':'com.com2us.smon.normal.freefull.apple.kr.ios.universal','device':'iPad5,4','did':str(random.randint(200000000,300000000)),'native_version':'Hub v.2.6.4','osversion':'10.2','platform':'ios','vendor_id':Tools().rndDeviceId()})
		self.registered()
		res=self.create()
		self.auth()
		return res['guest_uid'],res['did']