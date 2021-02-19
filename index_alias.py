from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost', port=9200)

# put_alias新增別名
es.indices.put_alias(index='school_members', name='school')