import requests
import json
import openpyxl

wk = openpyxl.Workbook()
sheet = wk.create_sheet()
resp = requests.get('https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1693747366565&loginType=3&uuid=122270672.1465280583.1690273724.1690285526.1693746518.3&productId=8452203&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1&bbtf=&shield=')
json_data = json.loads(resp.text)
comments = json_data['comments']
for item in comments:
    color = item['productColor']
    size = item['productSize']
    print(color + '_' + size)
    sheet.append([color, size])
    wk.save('京东销量最高的鞋子的颜色和大小.xlsx')
