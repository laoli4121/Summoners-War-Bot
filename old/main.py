import zlib
import base64
import json
import requests
import sys
import random
import os
import api
import crypt

s=requests.session()
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
s.proxies.update(proxies)
s.verify=False
s.headers.update({'User-Agent':'SMON_Kr/3.0.9.232005 CFNetwork/758.5.3 Darwin/15.6.0'})

def randomHex(n):
	return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])
	
def getLocation():
	return decrypt_response(s.get(url_location_c2).content,2 if '_c2.php' in url_location_c2 else 1)
	
def getServerStatus():
	data='H5dFyAJCZq0XPjVy+EXKzAFBljOGSavG/H7OunbeDlWx7+dFf+n6G46dJYMSHeQCzVrnEjktPNJD+1XboVHMDkC8dhtGQjzmDs6qrKD8Vtc='
	decrypt_response(s.post(url_server_status_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1)
	decrypt_response(s.post(url_version_info_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1)
	
def CheckLoginBlock():
	data=	'ffDzT4PTkBREOGro2FJjv2l1a8ZV6pgc8RXbFwnvkrxpqS1MXfm4HghMgE4AbqHA3UoDTTEKX0uAof3fP+UuwAlAFNLbq1v8TVSm81ldAANgo+4Qm1VGI6pL+hJzqcMpRcOb/HBXJ1MpqZnRVXGatlbpQ2p2xlE23ogvtRgQ2zGggXPzp0m2Pm/VeewcaMOrRAGa9leH5sfM7m0pRUvC8A=='
	return decrypt_response(s.post(url_gateway_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1) 

def BattleScenarioStart(region_id,stage_no,difficulty):
	data='''{
	"retry" : 0,
	"region_id" : %s,
	"helper_list" : [],
	"ts_val" : 1271247757,
	"infocsv" : "3.00.09",
	"proto_ver" : 10700,
	"wizard_id" : 4139926,
	"stage_no" : %s,
	"difficulty" : %s,
	"command" : "BattleScenarioStart",
	"channel_uid" : 90147775313,
	"session_key" : "90147775313",
	"unit_id_list" : [{
			"unit_id" : 2797656781
		}, {
			"unit_id" : 2797655858
		}, {
			"unit_id" : 2797661693
		}
	]
}'''%(region_id,stage_no,difficulty)
	data=encrypt_request(data,2)
	return decrypt_response(s.post(url_gateway_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1) 
	
def BattleScenarioResult(battle_key,opp_unit_status_list):
	data='''{
	"unit_id_list" : [{
			"pos_id" : 1,
			"unit_id" : 2797656781
		}, {
			"pos_id" : 2,
			"unit_id" : 2797655858
		}, {
			"pos_id" : 3,
			"unit_id" : 2797661693
		}
	],
	"battle_key" : %s,
	"ts_val" : 1271249938,
	"infocsv" : "3.00.09",
	"proto_ver" : 10700,
	"wizard_id" : 4139926,
	"clear_time" : 74159,
	"win_lose" : 1,
	"command" : "BattleScenarioResult",
	"position" : {
		"island_id" : 1,
		"pos_x" : 21,
		"pos_y" : 20
	},
	"channel_uid" : 90147775313,
	"session_key" : "90147775313",
	"opp_unit_status_list" : %s
}'''%(battle_key,opp_unit_status_list)
	data=encrypt_request(data,2)
	return api.decrypt_response(s.post(url_gateway_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1) 

def save(data,filename):
	with open(filename+'.json', 'w') as outfile:
		json.dump(data, outfile)	
	
def do(o):
	try:
		data= json.loads(decrypt_request(o,2))
		bns='_request'
	except:
		data= json.loads(decrypt_response(o,2))
		bns='_response'
	print data
	filename='dump\\'+data['command']+bns
	print data['command']
	save(data,filename)

def GuestLogin(idfa,adid,token,did,uid):
	data='''{
	"lang" : "eng",
	"idfv" : "%s",
	"uid" : %s,
	"binary_check" : "6e4f91b56a43191c5c775056d4341995",
	"did" : %s,
	"country" : "DE",
	"infocsv" : "3.00.09",
	"adid" : "%s",
	"proto_ver" : 10700,
	"device_name" : "iPad5,4",
	"os_version" : "9.3.3",
	"token" : "%s",
	"command" : "GuestLogin",
	"game_index" : 2623,
	"mac_address" : "02:00:00:00:00:00",
	"push" : 1,
	"channel_uid" : 90147805022,
	"create_if_not_exist" : 1,
	"app_version" : "3.0.7",
	"binary_size" : 9819776
}'''%(idfa,uid,did,adid,token)
	data=encrypt_request(data,2)
	return api.decrypt_response(s.post(url_gateway_c2,data=data).content,2 if '_c2.php' in url_location_c2 else 1) 
	
def decrypt_request(msg, version = 1):
	return crypt.decrypt_request(msg,version)
	
def decrypt_response(msg, version = 1):
	return crypt.decrypt_response(msg, version)
	
def encrypt_request(msg, version = 1):
	return crypt.encrypt_request(msg, version)
	
def saveAccount(data):
	with open('accounts.json', 'w') as outfile:
		json.dump(data, outfile)
		
def loadAccounts():
	if not os.path.isfile('accounts.json'):
		return {}
	with open('accounts.json') as data_file:    
		return json.load(data_file)
	
def getDid(advertising_id,vendor_id,did,android=False):
	if android:
		gameindex='2624'
	else:
		gameindex='2623'
	cake={'gameindex':gameindex,
			'advertising_id':advertising_id,
			'appid':'com.com2us.smon.normal.freefull.apple.kr.ios.universal',
			'device':'iPad5,4',
			'did':str(did),
			'native_version':'Hub v.2.4.2',
			'osversion':'9.3.3',
			'platform':'ios',
			'vendor_id':vendor_id}
	r=s.post(api.url_did,cookies=cake)
	data= json.loads(r.content)
	return data['guest_uid'],data['did']
	
def createAccount():
	idfa=str('%s-%s-%s-%s-%s'%(randomHex(8),randomHex(4),randomHex(4),randomHex(4),randomHex(12)))
	adid=str('%s-%s-%s-%s-%s'%(randomHex(8),randomHex(4),randomHex(4),randomHex(4),randomHex(12)))
	token=str('%s'%(randomHex(64)))
	uid,did= getDid(adid,idfa,random.randrange(200000000, 292403964, 2))
	data=json.loads(GuestLogin(idfa,adid,token,did,uid))
	print '[+]wizard_id: %s wizard_name: %s'%(data['wizard_info']['wizard_id'],data['wizard_info']['wizard_name'])
	accounts=loadAccounts()
	n={did:{'idfa':idfa,'adid':adid,'token':token,'did':did,'uid':uid}}
	accounts.update(n)
	saveAccount(accounts)
	
def device():
	idfv='4A5D22E5-ED06-4E6A-80AC-3F888C038869'
	uid='90147808987'
	did='212403964'
	adid='ED8CBC4E-8A00-40F7-ACC1-C49569886E8A'
	token='9d22f6f771747df4a190a72d2e53a1853d47970faeadb170000778315b3af383'.lower()
	#print api.command(api.CheckLoginBlock('90147808987'))
	wizard= api.command(api.GuestLogin(idfv,uid,did,adid,token))
	wizard = json.loads(wizard)
	#player info
	print '--------Player Info--------'
	print '[+]id: %s name: %s level: %s exp: %s'%(wizard['wizard_info']['wizard_id'],wizard['wizard_info']['wizard_name'],wizard['wizard_info']['wizard_level'],wizard['wizard_info']['experience'])
	print
	#building info
	building_list = wizard['building_list']
	unit_list = wizard['unit_list']
	quest_active = wizard['quest_active']
	#ach_list=[]
	#quests=[]
	#for quest in quest_active:
	#	ach_list.append({"current": 7, "ach_id": quest['quest_id'], "cond_id": 1})
	#	quests.append({"progressed": 7, "quest_id": quest['quest_id']})
	#	print quest['quest_id']	
	#api.command(api.UpdateAchievement(json.dumps(ach_list),wizard['wizard_info']['wizard_id'],uid))
	#api.command(api.UpdateDailyQuest(json.dumps(quests),wizard['wizard_info']['wizard_id'],uid))
	#exit()
	unit_list_dungeon=[]
	scenario_list = wizard['scenario_list']
	defense_unit_list = wizard['defense_unit_list']
	print '--------Player Buildings--------'
	for building in building_list:
		if building['gain_per_hour'] > 0:
			print '[+]building_id: %s harvest_available: %s'%(building['building_id'],building['harvest_available'])
			if building['harvest_available'] > 0:
				print '[+]collecting resources from: %s'%(building['building_id'])
				api.command(api.Harvest(building['building_id'],wizard['wizard_info']['wizard_id'],uid))
	print
	print '--------Player Units--------'
	for unit in unit_list:
		if len(unit_list_dungeon)<5:
			unit_list_dungeon.append({'unit_id':unit['unit_id']})
		print '[+]unit_id: %s unit_level: %s atk: %s def: %s experience: %s'%(unit['unit_id'],unit['unit_level'],unit['atk'],unit['def'],unit['experience'])
	print
	print '--------Player Scenario--------'
	for scenario in scenario_list:
		print '[+]region_id: %s difficulty: %s cleared: %s'%(scenario['region_id'],scenario['difficulty'],scenario['cleared'])
		for stage in scenario['stage_list']:
			print '[+]stage_no: %s cleared: %s'%(stage['stage_no'],stage['cleared'])
	print
	print '[!] clear stage ?'
	clear_stage = raw_input("Only y or n: ")
	if clear_stage == 'y':
		unit_id_list=[]
		unit_id_list_res=[]
		for idx,dunit in enumerate(defense_unit_list):
			unit_id_list.append({'unit_id':dunit['unit_id']})
			unit_id_list_res.append({'pos_id':idx+1,'unit_id':dunit['unit_id']})
		if stage['stage_no'] == 7:
			scenario['region_id']+=1
			stage['stage_no']=0
		response= api.command(api.BattleScenarioStart(0,scenario['region_id'],wizard['wizard_info']['wizard_id'],stage['stage_no']+1,scenario['difficulty'],uid,json.dumps(unit_id_list)))
		response = json.loads(response)
		if response['ret_code']!=0:
			print '[-]no energy'
			exit()
		battle_units = response['opp_unit_list']
		killed_units=[]
		rounds= len(battle_units)
		i=0
		while i < rounds:
			for bunits in battle_units[i]:
				killed_units.append({"unit_id":bunits['unit_id'],"result":2})
			i+=1
		battle_result =api.command(api.BattleScenarioResult(json.dumps(unit_id_list_res),response['battle_key'],wizard['wizard_info']['wizard_id'],13703,uid,json.dumps(killed_units)))
		battle_result = json.loads(battle_result)
		print battle_result['ret_code']
		print '[+]mana: %s'%(battle_result['reward']['mana'])
		if False:
			#print api.command(api.GetDungeonList(wizard['wizard_info']['wizard_id'],uid))
			#exit()
			response= api.command(api.BattleDungeonStart(5,0,8001,json.dumps(unit_list_dungeon),wizard['wizard_info']['wizard_id'],uid))
			response = json.loads(response)
			dungeon_unit_list = response['dungeon_unit_list']
			killed_units=[]
			rounds= len(dungeon_unit_list)
			i=0
			while i < rounds:
				for bunits in dungeon_unit_list[i]:
					killed_units.append({"unit_id":bunits['unit_id'],"result":2})
				i+=1
			dungeon_result= api.command(api.BattleDungeonResult(5,8001,json.dumps(unit_list_dungeon),response['battle_key'],wizard['wizard_info']['wizard_id'],180022,1,uid,json.dumps(killed_units)))
			dungeon_result = json.loads(dungeon_result)
			print dungeon_result['ret_code']
			print '[+]mana: %s'%(dungeon_result['reward']['mana'])		

def main():
	#idfv='4A5D22E5-ED06-4E6A-80AC-3F888C038869'
	#adid='ED8CBC4E-8A00-40F7-ACC1-C49569886E8A'
	#print getDid(idfv,adid,483340330,True)
	#exit()
	device()
	exit()
	if len(sys.argv)==1:
		createAccount()
		exit()
		units = data['unit_list']
		print '[+]found %s units:'%(len(units))
		for unit in units:
			print '[+]unit_id: %s atk: %s critical_damage: %s def: %s'%(unit['unit_id'],unit['atk'],unit['critical_damage'],unit['def'])
		u=1
		while u < 8:
			battle_data= json.loads(BattleScenarioStart(14,u,1))
			print '[+]battle_key: %s'%(battle_data['battle_key'])
			battle_units = battle_data['opp_unit_list']
			killed_units=[]
			rounds= len(battle_units)
			i=0
			while i < rounds:
				for bunits in battle_units[i]:
					killed_units.append({"unit_id":bunits['unit_id'],"result":2})
				i+=1
			BattleScenarioResult(battle_data['battle_key'],json.dumps(killed_units))
			u+=1
		#BattleScenarioResult(1475003205,json.dumps(killed_units))
	else:
		do(sys.argv[1])
	
if __name__=="__main__":
	main()