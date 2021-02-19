from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost', port=9200)

# es.indices.get 回傳index訊息
result = es.indices.get(index='school_members') #index指定要get哪個index的資訊
print(result)