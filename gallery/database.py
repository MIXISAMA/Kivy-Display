from collections import namedtuple
from typing import List

import pymysql

DataTuple = namedtuple('DataTuple', ['id', 'name', 'spread', 'age', 'url'])

# 配置
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'qpwoskxm',
    'database': 'kivygallery',
}





class MySql:
    def __enter__(self):
        self.conn = pymysql.Connect(**config)
        return self.conn.cursor()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

select_sql = '''
SELECT A.relic_id, relic_name, spread, age, data_origin_name
FROM rep_relic_base AS A
INNER JOIN rep_relic_data AS B ON A.relic_id = B.relic_id
INNER JOIN rep_data AS C ON C.data_id = B.data_id
WHERE data_type = 0
'''

def fetch_data():
    with MySql() as cursor:
        cursor.execute(select_sql)
        data = cursor.fetchall()
    return fake_data



fake_data = [
    {
        'id': 46,
        'name': '陶罐',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '唐(618~907)',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test1.jpeg',
            }
        ]
    },
    {
        'id': 47,
        'name': '瓷器',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '隋(581~618)',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test2.jpeg',
            }
        ]
    },
    {
        'id': 48,
        'name': '钱币',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '南北朝',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test3.jpeg',
            },
            {
                'type': 'img',
                'url': 'fakedata/test4.jpeg',
            }
        ]
    },
    {
        'id': 49,
        'name': '炊具',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '200万年以前',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test5.jpeg',
            },
            {
                'type': 'img',
                'url': 'fakedata/test6.jpeg',
            }
        ]
    },
    {
        'id': 52,
        'name': '瓦当',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '元(1206~1368)',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test7.jpeg',
            }
        ]
    },
    {
        'id': 53,
        'name': '石碑',
        'spread': '陕西省礼泉唐昭陵陪葬墓出土',
        'age': '汉',
        'media': [
            {
                'type': 'img',
                'url': 'fakedata/test8.jpeg',
            }
        ]
    }
]
clean_data = fetch_data()
if __name__ == '__main__':
    print(clean_data)