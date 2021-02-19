from elasticsearch import Elasticsearch
import json

# put_mapping 同一index新增mappings
def change_mappings(es):
    body = get_teacher_mappings()
    es.indices.put_mapping(index='school_members', body=body)

def get_teacher_mappings():
    mappings = {
        "properties": {
            "tid": {
                "type": "keyword"
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
    es = Elasticsearch(hosts='localhost', port=9200)
    
    change_mappings(es)