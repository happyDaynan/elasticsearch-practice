from elasticsearch import Elasticsearch
import json

"""
# 設定mappings
{
    "mappings":{
        "properties":{
            "sid":{
                "type": "integer"
            },
            "name":{
                "type": "text"
            },
            "age":{
                "type": "integer"
            },
            "class":{
                "type": "keyword"
            }
        }
    }    
}

# 設定settings
{
    "setting":{
        "index":{
            # 設定主分片，只能在建立前設定好
            "number_of_shards":3,
            # 設定副本分片，之後能修改
            "number_of_replicas":1
        }
    }
}
"""

def create_index(es):
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mappings()
    # print(json.dumps(body))
    # es.indices.create(index='school_members', body=body)

def get_setting():
    settings = {
        "index":{
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
    }

    return settings



def get_mappings():
    mappings = {
        "properties":{
            "sid":{
                "type": "integer"
            },
            "name":{
                "type": "text"
            },
            "age":{
                "type": "integer"
            },
            "class":{
                "type": "keyword"
            }
        }
    }

    return mappings

# put_mapping 同一index新增mappings
def change_mappings(es):
    body = get_teacher_mappings()
    es.indices.put_mapping(index='school_members', body=body)

def get_teacher_mappings():
    mappings = {
        "properties": {
            "tid": {
                "type": "integer"
            },
            "name": {
                "type": "text"
            },
            "age": {
                "type": "integer"
            },
            "class": {
                "type": "keyword"
            },
            "salary": {
                "type": "integer"
            }
        }
    }
    return mappings



if __name__ == "__main__":
    # 建立連結
    es = Elasticsearch(hosts='localhost', port=9200)
    # 新增index
    # create_index(es)

    # 增加mappings
    # change_mappings(es)

    # put_alias新增別名
    es.indices.put_alias(index='school_members', name='school')
    # delete_alias 刪除別名
    # es.indices.delete_alias(index='school_members', name='school')

    # es.indices.get 回傳index訊息
    result = es.indices.get(index='school_members') #index指定要get哪個index的資訊
    print(result)

    # es.indices.exists 查看index是否存在
    # result = es.indices.exists(index='school_members')
    # print(result)
    