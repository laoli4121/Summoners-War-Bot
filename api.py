import crypt
import requests

#setup
url_location_c2='http://summonerswar-eu.com2us.net/api/location_c2.php'
url_server_status_c2 ='http://summonerswar-eu.qpyou.cn/api/server_status_c2.php'
url_version_info_c2 ='http://summonerswar-eu.qpyou.cn/api/version_info_c2.php'
url_gateway_c2 ='http://summonerswar-eu.qpyou.cn/api/gateway_c2.php'
url_did='http://api.qpyou.cn/guest/create'
#end

s=requests.session()
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
s.proxies.update(proxies)
s.verify=False
s.headers.update({'User-Agent':'SMON_Kr/3.0.9.232005 CFNetwork/758.5.3 Darwin/15.6.0'})

infocsv='3.00.18'
proto_ver=10710
game_index=2623
binary_check='059b4fc2a71c7146ea20a506257900c7'
app_version='3.0.9'

def decrypt_request(msg, version = 1):
	return crypt.decrypt_request(msg,version)
	
def decrypt_response(msg, version = 1):
	return crypt.decrypt_response(msg, version)
	
def encrypt_request(msg, version = 1):
	return crypt.encrypt_request(msg, version)

def command(data):
	return decrypt_response(s.post(url_gateway_c2,data=encrypt_request(data,2)).content,2 if '_c2.php' in url_location_c2 else 1) 

def CheckLoginBlock(uid):
	data='''{"infocsv": "%s", "proto_ver": %s, "command": "CheckLoginBlock", "game_index": %s, "channel_uid": %s, "session_key": "%s"}'''%(infocsv,proto_ver,game_index,uid,uid)
	return data
	
def SetWizardName(wizard_id,wizard_name,uid):
	data='''{"ts_val": 1271184474, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "wizard_name": "%s", "command": "SetWizardName", "channel_uid": %s, "session_key": "%s"}'''%(infocsv,proto_ver,wizard_id,wizard_name,uid,uid)
	return data
	
def BattleScenarioStart(retry,region_id,wizard_id,stage_no,difficulty,channel_uid,unit_id_list):
	data='''{"retry": %s, "region_id": %s, "helper_list": [], "ts_val": 1271184287, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "stage_no": %s, "difficulty": %s, "command": "BattleScenarioStart", "channel_uid": %s, "session_key": "%s", "unit_id_list": %s}'''%(retry,region_id,infocsv,proto_ver,wizard_id,stage_no,difficulty,channel_uid,channel_uid,unit_id_list)
	return data
	
def BattleScenarioResult(unit_id_list,battle_key,wizard_id,clear_time,channel_uid,opp_unit_status_list):
	data='''{"unit_id_list": %s, "battle_key": %s, "ts_val": 1271184290, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "clear_time": %s, "win_lose": 1, "command": "BattleScenarioResult", "position": {"island_id": 1, "pos_x": 21, "pos_y": 21}, "channel_uid": %s, "session_key": "%s", "opp_unit_status_list": %s}'''%(unit_id_list,battle_key,infocsv,proto_ver,wizard_id,clear_time,channel_uid,channel_uid,opp_unit_status_list)
	return data
	
def BattleDungeonStart(stage_id,retry,dungeon_id,unit_id_list,wizard_id,channel_uid):
	data='''{"stage_id": %s, "retry": %s, "dungeon_id": %s, "unit_id_list": %s, "helper_list": [], "ts_val": 1271190999, "cash_used": 0, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "command": "BattleDungeonStart", "channel_uid": %s, "session_key": "%s"}'''%(stage_id,retry,dungeon_id,unit_id_list,infocsv,proto_ver,wizard_id,channel_uid,channel_uid)
	return data
	
def Harvest(building_id,wizard_id,channel_uid):
	data='''{"building_id": %s, "ts_val": 1271183978, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "command": "Harvest", "channel_uid": %s, "session_key": "%s"}'''%(building_id,infocsv,proto_ver,wizard_id,channel_uid,channel_uid)
	return data
	
def UpdateAchievement(ach_list,wizard_id,channel_uid):
	data='''{"ach_list": %s, "ts_val": 1271195538, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "command": "UpdateAchievement", "channel_uid": %s, "session_key": "%s"}'''%(ach_list,infocsv,proto_ver,wizard_id,channel_uid,channel_uid)
	return data
	
def UpdateDailyQuest(wizard_id,quests,channel_uid):
	data='''{"ts_val": 1271195062, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "command": "UpdateDailyQuest", "quests": %s, "channel_uid": %s, "session_key": "%s"}'''%(infocsv,proto_ver,quests,wizard_id,channel_uid,channel_uid)
	return data
	
def GetDungeonList(wizard_id,channel_uid):
	data='''{"ts_val": 1271190179, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "command": "GetDungeonList", "channel_uid": %s, "session_key": "%s"}'''%(infocsv,proto_ver,wizard_id,channel_uid,channel_uid)
	return data
	
def BattleDungeonResult(stage_id,dungeon_id,unit_id_list,battle_key,wizard_id,clear_time,island_id,channel_uid,opp_unit_status_list):
	data='''{"stage_id": %s, "pos_y": 20, "dungeon_id": %s, "unit_id_list": %s, "battle_key": %s, "ts_val": 1271190163, "infocsv": "%s", "proto_ver": %s, "wizard_id": %s, "clear_time": %s, "island_id": %s, "pos_x": 18, "win_lose": 1, "command": "BattleDungeonResult", "channel_uid": %s, "session_key": "%s", "opp_unit_status_list": %s}'''%(stage_id,dungeon_id,unit_id_list,battle_key,infocsv,proto_ver,wizard_id,clear_time,island_id,channel_uid,channel_uid,opp_unit_status_list)
	return data
	
def GuestLogin(idfv,uid,did,adid,token):
	data='''{"lang": "eng", "idfv": "%s", "uid": %s, "binary_check": "%s", "did": %s, "country": "DE", "infocsv": "%s", "adid": "%s", "proto_ver": %s, "device_name": "iPad5,4", "os_version": "9.3.3", "token": "%s", "command": "GuestLogin", "game_index": %s, "mac_address": "02:00:00:00:00:00", "push": 1, "channel_uid": %s, "create_if_not_exist": 1, "app_version": "%s", "binary_size": 9364464}'''%(idfv,uid,binary_check,did,infocsv,adid,proto_ver,token,game_index,uid,app_version)
	return data