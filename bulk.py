
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

"""
批量匯入資料 bulk
bulk使用，透過action這個結構
action基本結構
{
    "_op_type": "index", # 執行動作index,delete,update
    "_index": "school_members", # 指定index
    "_id": 1, # 指定id，如不指定會動生成 
    # 文檔內容
    "_source": {    
        "sid": "s1090101",
        "name": "小名",
        "age": 18,
        "class": "資工-1"
        }
}
"""
def load_datas():
    actions = list()
    with open('student.csv', 'r', encoding='utf-8') as f:
        for data in f.readlines():
            sid, name, age, class_ = data.replace('\n', '').split(',')
            actions.append(
                {
                  "_index": "school_members",
                  "_op_type": "index",
                  "_source": {
                      "sid": sid,
                      "name": name,
                      "age": int(age),
                      "class": class_
                  }  
                }
            )
    return actions

if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)
    data = load_datas()
    print(json.dumps(data, ensure_ascii=False))
    helpers.bulk(es, data) 
