# ISKG
intelligent service knowledge graph project

#### 相关业务资料：
XX智能服务的知识图谱抽取和存储文档v1.3.1.docx  
XX智能服务的知识图谱模型设计文档v3.1.docx

#### 论文： 
知识图谱embedding，补全(实体、关系预测)的相关论文、survey。   
主要实现论文：   
**Learning Attention-based Embeddings for Relation Prediction in Knowledge Graph**   
repo: https://github.com/deepakn97/relationPrediction   
blog：https://deepakn97.github.io/blog/2019/Knowledge-Base-Relation-Prediction/   
**convKB**   
repo：https://github.com/daiquocnguyen/ConvKB

##### input_data：  
从neo4j私有数据导出后，处理好的实体、关系、三元组编号。   
格式为：   
头实体编号 尾实体编号 关系编号   
entity2id/xxx2id   
neo4j_id 编号 relation2id  
or关系名称 编号   
ISKG_maintain.csv 是从neo4j中导出的，见数据处理。movies.csv是一个简单的domo格式示例。

**graph.db：**   
neo4j私有数据备份，下载neo4j community版本可导入。   
导入方法：可下载neo4j desktop，方便管理、安装apoc插件 http://neo4j.com.cn/topic/59c27adf1f16d3b94d3274c6

**数据处理：**   
导出维修服务相关的知识图谱到csv  
match(n:实例节点:维修服务)-[r]->(m:实例节点:维修服务)   
where not n:智能头盔 and not m:智能头盔   
with collect(distinct n) as heads, collect(distinct m) as tails, collect(r) as rels   
CALL apoc.export.csv.data(heads+tails, rels, "ISKG_maintain.csv", {})   
YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data   
RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data 注：这个cypher语句导出的数据，因为(h, r, t) (t, x, y)，t可能出现两次，所有在数据处理时实体要去重。 处理为：input_data格式 python处理代码见input_data/preteat.ipynb

**补充论文：**   
https://weizhixiaoyi.com/paper.html
