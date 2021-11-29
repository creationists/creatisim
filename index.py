from bs4 import BeautifulSoup
import requests
import json
# get category

def get_category(url):
    new_cate = []
    data = requests.get(url).json()
    for sub in data['data']:
        new_cate.append({'id': sub['id'], 'name':sub['name']})
    return new_cate

def open_json(path):

    f = open(path)
    data = json.load(f)
    f.close()
    return data

def save_json(name,save_data):
    with open(name, "w",encoding="UTF-8") as f: 
        json.dump(save_data, f,ensure_ascii=False)
        
first_index = open_json("/workspace/crawl/second_index.json")
total=[]
for item in first_index:
    sub_list = []
    for sub_num in item['sub_cate']:
        url = "https://api.itemscout.io/api/category/{}/subcategories".format(sub_num['id'])
        data = get_category(url)
        sub_list.append({'id':sub_num['id'],'name':sub_num['name'],'detail':data})
    total.append({'id':item['id'],'name':item['name'],'sub_cate':sub_list})

save_json('detail_index.json',total)
