import requests
from crypt import Crypter
import json
import time
from collections import OrderedDict

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class API(object):
	def __init__(self,did):
		self.crypter=Crypter()
		self.s=requests.session()
		self.s.verify=False
		self.s.headers.update({'User-Agent':'SMON_Kr/3.7.0.37000 CFNetwork/808.2.16 Darwin/16.3.0'})
		self.game_index=2623
		self.proto_ver=11000
		self.app_version='3.7.0'
		self.c2_api='http://summonerswar-gb.qpyou.cn/api/gateway_c2.php'
		self.uid=90173833053
		self.did=did

	def setIDFA(self,id):
		self.idfa=id
		
	def log(self,msg):
		print '[%s]:%s'%(time.strftime('%H:%M:%S'),msg)
		
	def callAPI(self,path,data):
		if type(data)<>str:
			data=json.dumps(data).replace(' ','')
		data=self.crypter.encrypt_request(data,2 if '_c2.php' in path else 1)
		res=self.s.post(path,data)
		return json.loads(self.crypter.decrypt_response(res.content,2 if '_c2.php' in path else 1))

	def getServerStatus(self):
		data={}
		data['game_index']=self.game_index
		data['proto_ver']=self.proto_ver
		data['channel_uid']=0
		return self.callAPI('http://summonerswar-gb.qpyou.cn/api/server_status_c2.php',data)

	def getVersionInfo(self):
		data={}
		data['game_index']=self.game_index
		data['proto_ver']=self.proto_ver
		data['channel_uid']=0
		res= self.callAPI('http://summonerswar-gb.qpyou.cn/api/version_info_c2.php',data)
		self.parseVersionData(res['version_data'])
		return res
		
	def parseVersionData(self,input):
		for v in input:
			if v['topic']=='protocol':
				self.log('found proto_ver:%s'%(v['version']))
				self.proto_ver=v['version']
			if v['topic']=='infocsv':
				self.log('found infocsv:%s'%(v['version']))
				self.infocsv=v['version']
	
	def base_data(self,cmd,kind=1):
		if kind == 1:
			data=OrderedDict([('command',cmd),('game_index',self.game_index),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid)])
		elif kind ==2:
			data=OrderedDict([('command',cmd),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.uid),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454877')])
		return data

	def CheckLoginBlock(self):
		data=self.base_data('CheckLoginBlock')
		return self.callAPI(self.c2_api,data)

	def GetDailyQuests(self):
		data=self.base_data('GetDailyQuests',2)
		return self.callAPI(self.c2_api,data)

	def GetMiscReward(self):
		data=self.base_data('GetMiscReward',2)
		return self.callAPI(self.c2_api,data)

	def GetMailList(self):
		data=self.base_data('GetMailList',2)
		return self.callAPI(self.c2_api,data)

	def GetArenaLog(self):
		data=self.base_data('GetArenaLog',2)
		return self.callAPI(self.c2_api,data)

	def ReceiveDailyRewardSpecial(self):
		data=self.base_data('ReceiveDailyRewardSpecial',2)
		return self.callAPI(self.c2_api,data)

	def GetFriendRequest(self):
		data=self.base_data('GetFriendRequest',2)
		return self.callAPI(self.c2_api,data)

	def GetChatServerInfo(self):
		data=self.base_data('GetChatServerInfo',2)
		return self.callAPI(self.c2_api,data)

	def getRtpvpRejoinInfo(self):
		data=self.base_data('getRtpvpRejoinInfo',2)
		return self.callAPI(self.c2_api,data)

	def GetNoticeDungeon(self):
		data=self.base_data('GetNoticeDungeon',2)
		return self.callAPI(self.c2_api,data)

	def GetNoticeChat(self):
		data=self.base_data('GetNoticeChat',2)
		return self.callAPI(self.c2_api,data)

	def GetNpcFriendList(self):
		data=self.base_data('GetNpcFriendList',2)
		return self.callAPI(self.c2_api,data)

	def SetWizardName(self,name):
		data=OrderedDict([('command','SetWizardName'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454178'),('wizard_name',name)])
		return self.callAPI(self.c2_api,data)

	def UpdateEventStatus(self,event_id):
		data=OrderedDict([('command','UpdateEventStatus'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454202'),('event_id',event_id)])
		return self.callAPI(self.c2_api,data)

	def GetEventTimeTable(self):
		data=OrderedDict([('command','GetEventTimeTable'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454203'),('lang','1'),('app_version',self.app_version)])
		return self.callAPI(self.c2_api,data)

	def Harvest(self,building_id):
		data=OrderedDict([('command','Harvest'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454214'),('building_id',building_id)])
		return self.callAPI(self.c2_api,data)

	def TriggerShopItem(self,trigger_id):
		data=OrderedDict([('command','TriggerShopItem'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454226'),('trigger_id',trigger_id)])
		return self.callAPI(self.c2_api,data)

	def UpdateAchievement(self,ach_list):
		data=OrderedDict([('command','TriggerShopItem'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454226'),('ach_list',ach_list)])
		return self.callAPI(self.c2_api,data)

	def UpdateDailyQuest(self,quests):
		data=OrderedDict([('command','TriggerShopItem'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454226'),('quests',quests)])
		return self.callAPI(self.c2_api,data)

	def BattleScenarioStart(self,region_id,stage_no,difficulty,unit_id_list):
		data=OrderedDict([('command','BattleScenarioStart'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454271'),('region_id',region_id),('stage_no',stage_no),('difficulty',difficulty),('unit_id_list',unit_id_list),('helper_list','[]'),('mentor_helper_list','[]'),('npc_friend_helper_list','[]'),('retry','0')])
		return self.callAPI(self.c2_api,data)

	def BattleScenarioResult(self,battle_key,opp_unit_status_list,unit_id_list,position):
		data=OrderedDict([('command','BattleScenarioResult'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454039'),('battle_key',battle_key),('win_lose','1'),('opp_unit_status_list',opp_unit_status_list),('unit_id_list',unit_id_list),('position',position),('clear_time','34524'),('retry','0')])
		return self.callAPI(self.c2_api,data)

	def SummonUnit(self,building_id,pos_arr):
		data=OrderedDict([('command','SummonUnit'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454069'),('building_id',building_id),('mode','1'),('pos_arr',pos_arr)])
		return self.callAPI(self.c2_api,data)

	def EquipRune(self,rune_id,unit_id):
		data=OrderedDict([('command','EquipRune'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454084'),('rune_id',rune_id),('unit_id',unit_id)])
		return self.callAPI(self.c2_api,data)

	def UpgradeRune(self,rune_id,unit_id):
		data=OrderedDict([('command','UpgradeRune'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454107'),('rune_id',rune_id),('upgrade_curr','0'),('cash_used','0'),('stone_used','0')])
		return self.callAPI(self.c2_api,data)

	def BuyShopItem(self,item_id):
		data=OrderedDict([('command','BuyShopItem'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454125'),('item_id',item_id),('island_id','1'),('pos_x','21'),('pos_y','20')])
		return self.callAPI(self.c2_api,data)

	def ClaimAchievementReward(self,ach_id):
		data=OrderedDict([('command','ClaimAchievementReward'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454428'),('ach_id',ach_id)])
		return self.callAPI(self.c2_api,data)

	def SacrificeUnit(self,target_id,source_list):
		data=OrderedDict([('command','SacrificeUnit'),('wizard_id',self.wizard_id),('session_key',self.uid),('proto_ver',self.proto_ver),('infocsv',self.infocsv),('channel_uid',self.uid),('ts_val','1178454138'),('target_id',target_id),('island_id','1'),('building_id','0'),('pos_x','8'),('pos_y','14'),('source_list',source_list)])
		return self.callAPI(self.c2_api,data)

	def setUser(self,input):
		self.user=input
	
	def getUserInfo(self):
		return 'id:%s username:%s energy:%s mana:%s crystal:%s'%(self.user['wizard_info']['wizard_id'],self.user['wizard_info']['wizard_name'],self.user['wizard_info']['wizard_energy'],self.user['wizard_info']['wizard_mana'],self.user['wizard_info']['wizard_crystal'])
		
	def GuestLogin(self):
		data=OrderedDict([('command','GuestLogin'),('game_index',self.game_index),('proto_ver',self.proto_ver),('app_version',self.app_version),('infocsv',self.infocsv),('uid',self.uid),('channel_uid',self.uid),('did',self.did),('push','1'),('is_emulator','0'),('country','DE'),('lang','eng'),('lang_game','1'),('mac_address','02:00:00:00:00:00'),('device_name','iPad54'),('os_version','10.2'),('token','0000000000000000000000000000000000000000000000000000000000000000'),('idfv',self.idfa),('adid','00000000-0000-0000-0000-000000000000'),('binary_size','10347504'),('binary_check','00ebb9ec2dc09ed93c042b35c4b51590'),('create_if_not_exist','1')])
		res= self.callAPI(self.c2_api,data)
		self.setUser(res)
		self.log(self.getUserInfo())
		return res
		
	def completeTutorial(self):
		pass
		
		
if __name__ == "__main__":
	a=API(229313295)
	a.setIDFA("FE81F453-B667-44F3-A077-BAAB4BAA25C0")
	a.getServerStatus()
	a.getVersionInfo()
	a.CheckLoginBlock()
	a.GuestLogin()