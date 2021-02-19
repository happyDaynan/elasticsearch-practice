from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='localhost', port=9200)

es.indices.delete(index='school_members')