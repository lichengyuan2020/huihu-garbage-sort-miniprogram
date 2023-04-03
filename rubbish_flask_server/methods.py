from flask import request
import json
def to_Data():
    # data = request.get_data()  # 获取前端数据
    # data = str(data, 'utf-8')  # 转utf-8
    # data = json.loads(data)  # json转字典
    data = json.loads(request.get_data().decode("utf-8"))
    if data:
        return data
    else:
        return {}

def to_Json(list = None):
    if list:
        data = json.dumps(list, ensure_ascii = False)
    else:
        data = "0"
    return data