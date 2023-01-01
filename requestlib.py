import requests
import json


r = requests.get('https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=20221026130839175716859&sn=SVT7CYCWCP')

library = r.json()
result = library.get('result')

def updateTime():
	return result.get('uploadTime')
	# print(json.dumps(library, indent=2)) 
	# print(result.get('uploadTime'))
	# print(type(library)) 

