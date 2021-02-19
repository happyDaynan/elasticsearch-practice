from elasticsearch import Elasticsearch
import json

def create_index(es):
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mappings()
    print(json.dumps(body))
    es.indices.create(index='school_members', body=body)

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
                "type": "keyword"
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



if __name__ == "__main__":
    # 建立連結
    es = Elasticsearch(hosts='localhost', port=9200)
    # 新增index
    create_index(es)

 