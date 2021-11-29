from bs4 import BeautifulSoup
import tablib
import requests
import json 
# get category

def make_newsheet(name):
    new_sheet = tablib.Dataset(title = name,headers=['Name', 'product_cnt', 'search_cnt'])
    return new_sheet

def get_category(url):
    new_cate = []
    data = requests.get(url).json()
    for sub in data['data']:
        new_cate.append({'id': sub['id'], 'name':sub['name']})
    return new_cate

def get_detail(url,name):
    para = {"duration": "30d",
    "genders": "m",
    "ages": "10,60"}
    data = requests.post(url, data = para).json()
    #시트 이름 추가
    dataTab = make_newsheet(name)
    for num,values in data['data']['data'].items():
        try: 
            if values['prdCnt']/values['monthly']['total'] <6 :
                dataTab.append((values['keyword'],values['prdCnt'],values['monthly']['total']))
        except:
            pass
    return dataTab
def open_json(path):

    f = open(path)
    data = json.load(f)
    f.close()
    return data

def save_json(name,save_data):
    with open(name, "w",encoding="UTF-8") as f: 
        json.dump(save_data, f,ensure_ascii=False)
        
first_index = open_json("/workspace/crawl/detail_index.json")

book = tablib.Databook()


for item in first_index:
    for sub_num in item['sub_cate']:
        if item['id'] == 168 :
            break
        for detail_num in sub_num['detail']:
            url = "https://api.itemscout.io/api/category/{}/data".format(detail_num['id'])
            data = get_detail(url,detail_num['name'])
            book.add_sheet(data)
        break
    break

with open('output_total.xlsx', 'wb') as f:
    f.write(book.export('xlsx'))

