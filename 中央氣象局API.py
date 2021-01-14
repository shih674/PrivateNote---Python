# write by 674@2021/01/14
# version 1.0.0

import requests

# 中央氣象局API Document https://opendata.cwb.gov.tw/dist/opendata-swagger.html
api_type = "O-A0003-001"  # 局屬氣象站 - 現在天氣觀測報告
auth_code = "<apply-your-own-code>>"  # 請自行上網申請
stationID = "466900"  # 觀測站編號 https://e-service.cwb.gov.tw/wdps/obs/state.htm
api_url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{api_type}?Authorization={auth_code}&stationId={stationID}"
res = requests.get(api_url)

# print(res.json())  # 印出結果

# 抓取天氣觀測數據
target = res.json()['records']['location'][0]['weatherElement']
pair = {}
for ele in target:
    pair[ele['elementName']] = ele['elementValue']
    print(f"{ele['elementName']}\t：{ele['elementValue']}")
target = pair
print(res.json()['success'])  # 檢視回傳是否成功
print('天氣:', target)

# 解析json用工具
# print(type(target))
# if type(target) == dict:
#     print(target.keys())
# if type(target) == list:
#     print(len(target))
