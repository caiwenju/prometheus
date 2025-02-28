from prometheus_client import start_http_server, Gauge
import mysql.connector
import time

# 创建一个 Prometheus 指标，使用 Gauge 类型来表示实时的数值
process_name_gauge = Gauge('process_name_info', 'Information about process',
                           ['process_name', 'version', 'field1_name', 'field2_name'])


def fetch_mysql_data():
    # 连接到 MySQL 数据库
    conn = mysql.connector.connect(
        host="192.168.0.17",  # MySQL 主机
        port=43306,  # MySQL 端口
        user="root",  # MySQL 用户
        password="mysql",  # MySQL 密码
        database="szyg_portal"  # 目标数据库
    )
    cursor = conn.cursor(dictionary=True)

    # 执行查询
    cursor.execute("SELECT process_name, version, field1_name, field1_value, field2_name, field2_value FROM prometheus")

    # 获取查询结果
    rows = cursor.fetchall()

    # 将查询结果转换为 Prometheus 指标
    for row in rows:
        # 设置 Gauge 值
        process_name_gauge.labels(
            process_name=row['process_name'],
            version=row['version'],
            field1_name=row['field1_name'],
            field2_name=row['field2_name']
        ).set(1)  # 用 `1` 作为指标的值

    cursor.close()
    conn.close()


if __name__ == '__main__':
    # 启动一个 HTTP 服务来暴露指标
    start_http_server(8000)  # Prometheus 将通过 9104 端口抓取数据

    # 每隔 10 秒执行一次数据抓取
    while True:
        fetch_mysql_data()
        time.sleep(10)  # 每 10 秒抓取一次数据
