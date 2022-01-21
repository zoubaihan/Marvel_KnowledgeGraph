# Marvel_KnowledgeGraph

复旦2021秋知识图谱课程大作业（15组）：漫威超级英雄知识图谱与智能问答项目
![image](https://user-images.githubusercontent.com/60840371/150555147-579fd3bd-d5f5-4312-82a8-77abfb912903.png)

项目主页

![image](https://user-images.githubusercontent.com/60840371/150555187-c2e04265-7986-462d-9ae2-ed3a39b559a0.png)

知识图谱展示
![image](https://user-images.githubusercontent.com/60840371/150555259-a3ee1573-3d4f-46a9-8d4d-8d90e8c2990d.png)


配置环境以及安装neo4j，python版本需为3.6

控制台输入 "neo4j console" 启动neo4j

修改“KG_Marvel\neo_db\config.py”中的用户名密码

解压“KG_Marvel\KGQA\ltp_data_v3.4.0.zip”,压缩包资源在百度云。

修改“KG_Marvel\KGQA\ltp.py”中的模型路径（需用绝对路径）

运行“KG_Marvel\neo_db\creat_graph.py”，将关系传入数据库

运行 "KG_Marvel\app.py"

浏览器输入“http://localhost:5000/” 进入知识图谱。

