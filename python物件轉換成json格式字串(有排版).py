'''
使用json套件，在不必輸出成檔案的情況下，印出漂亮的json資料格式。

作者； 674
修改紀錄：
    20210221 - 初版完成
'''

import json

python_object = {
    'a': 10,
    'b': [1, 2, 3, 4],
    'c': {
        'ken': 27,
        'amber': 26
    }}

json_object = json.dumps(python_object, indent=4)

print(json_object)
