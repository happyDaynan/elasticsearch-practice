from elasticsearch import Elasticsearch
import json

"""
# 搜尋age=20
def get_query():
    query = {
        "query": {
            "bool": {
                "must": {
                    "term": {
                        "age": 20
                    }
                }
            }
        }
    }
    return query
"""

# 搜尋age=20，排除 sid = 1090103
def get_query():
    query = {
        "query": {
                "bool": {
                    "must": {
                        "term": {
                            "age": 20
                        }
                    },
                    "must_not":{
                        "term": {
                            "sid" : 1090103
                        }
                    }
                }
        }
    }
    return query



if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)
    query = get_query()
    result = es.search(index='school', body=query)
    print(json.dumps(result, ensure_ascii=False))