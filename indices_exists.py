from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost', port=9200)
# es.indices.exists 查看index是否存在
result = es.indices.exists(index='school_members')
print(result)