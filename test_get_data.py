import json

import requests

prometheus_url = "http://192.168.0.16:9090/api/v1/query"

# 定义查询语句
query = 'process_name_info{process_name="a",version="1.0"}'

# 发送 GET 请求到 Prometheus API
response = requests.get(prometheus_url, params={'query': query})

# 检查响应是否成功
if response.status_code == 200:
    # 解析 JSON 数据
    data = response.json()
    # 打印返回的数据
    print("Query Result:", json.dumps(data, indent=4))
else:
    print("Failed to retrieve data. HTTP Status Code:", response.status_code)
