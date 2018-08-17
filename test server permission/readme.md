## 测试是否有权限，服务器的连接性。

1. 先把所有的服务器 IP 地址放入 hosts
2. 运行 ansible ping 测试命令
3. 把 terminal 返回的信息复制粘贴到 failed_host.csv
4. 运行 filter_host.py 过滤得到失败的 IP, 将 IP 粘贴到 hosts [failed]分组
5. 重新运行 ansible ping 测试 [failed]分组  

几次迭代后，得到所有的不可达 IP 地址