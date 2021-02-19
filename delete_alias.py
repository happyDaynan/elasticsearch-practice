from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost', port=9200)

# delete_alias 刪除別名
es.indices.delete_alias(index='school_members', name='school')