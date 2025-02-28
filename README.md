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


三、示例数据
插入测试数据
连接到 MySQL 并插入一些测试数据：

sql
Copy
USE mydatabase;

CREATE TABLE orders (
  id INT PRIMARY KEY,
  amount DECIMAL(10, 2),
  status VARCHAR(20)
);

CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);

INSERT INTO orders (id, amount, status) VALUES
(1, 100.50, 'completed'),
(2, 200.00, 'pending');

INSERT INTO users (id, name, age) VALUES
(101, 'Alice', 25),
(102, 'Bob', 30);
