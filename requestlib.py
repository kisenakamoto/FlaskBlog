import requests

r = requests.get('https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=20221026130839175716859&sn=SVT7CYCWCP')

library = r.json()
result = library.get('result')
# result = library['result']
print(library) 
print('\n', result.get('uploadTime'))
