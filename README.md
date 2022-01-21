# Marvel_KnowledgeGraph
知识图谱课程大作业：漫威超级英雄知识图谱与智能问答项目
知识图谱课程大作业：漫威超级英雄知识图谱与智能问答项目
配置环境以及安装neo4j，python版本需为3.6
控制台输入 "neo4j console" 启动neo4j
修改“KG_Marvel\neo_db\config.py”中的用户名密码
解压“KG_Marvel\KGQA\ltp_data_v3.4.0.zip”
修改“KG_Marvel\KGQA\ltp.py”中的模型路径（需用绝对路径）
运行“KG_Marvel\neo_db\creat_graph.py”，将关系传入数据库
运行 "KG_Marvel\app.py"
浏览器输入“http://localhost:5000/” 进入知识图谱。
