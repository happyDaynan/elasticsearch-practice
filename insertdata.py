from elasticsearch import Elasticsearch

def load_datas():
    datas = list()
    with open('student.csv', 'r', encoding='utf-8') as f:
        for data in f.readlines():
            sid, name, age, class_ = data.replace('\n', '').split(',')

            datas.append(
                {
                    "sid": sid,
                    "name": name,
                    "age": int(age),
                    "class": class_
                }
            )

    return datas

def create_data(es, datas):
    for data in datas:
        es.index(index='school', body= data)

if __name__ == "__main__":
    es = Elasticsearch(hosts='localhost', port=9200)
    # datas = load_datas()
    # create_data(es, datas)

    result = es.indices.get(index='school_members') #index指定要get哪個index的資訊
    print(result) 
