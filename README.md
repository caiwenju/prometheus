# prometheus
prometheus
一、启动服务：
在项目目录中运行以下命令：

bash
Copy
docker-compose up -d

二、验证服务：

MySQL：可以通过 mysql -h 127.0.0.1 -u myuser -pmypassword mydatabase 连接到 MySQL。

MySQL Exporter：访问 http://localhost:9104/metrics，检查是否生成了自定义指标。

Prometheus：访问 http://localhost:9090，在 Prometheus 的 Web UI 中查询指标（如 orders_data_amount）。

Grafana：访问 http://localhost:3000，使用默认用户名 admin 和密码 admin 登录，配置 Prometheus 数据源并创建仪表板。


三、自定义export 的脚本exporter.py的使用说明
prometheus 会定期从 exporter.py 脚本中抓取指标，并将其存储，所以 exporter.py 脚本中的指标在每一次采集时返回的值决定了 prometheus 
中的指标值，可以从 exporter.py 控制时间戳的返回逻辑，从而控制 prometheus 中api聚合等逻辑的结果。