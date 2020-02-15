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


#### 数据处理：   
**data：**  
1.从neo4j私有数据导出ISKG_maintain.csv，处理为 (头实体编号 尾实体编号 关系编号) 格式。  
2.data/input_data_0126和0128都是相同的数据源，只是在分test/valid的时候有些区别，code见数据预处理文件夹。  
3.valid2id.txt，从ISKG_maintain.csv导出的三元组编号，csv中的实体id时neo4j中id，对该id排序后从0-n重新编号，见entity2id。关系按照中文从0-n编号，见relation2id。  
4.1-1.txt,1-n.txt,n-1.txt,n-n.txt，type_constrain.txt使用n-n.py产出，\*-\*.txt为test2id.txt中关系类别，type_constrain描述关系两边可出现哪些实体，可用于thunlp负例替换使用。  
5.目前用的**数据集是data/input0202_bs**, 其中entity2vec是entity2id对应训练好的向量，relation2vec同理。  
**graph.db：**   
neo4j私有数据备份，下载neo4j community版本可导入。   
导入方法：可下载neo4j desktop，方便管理、安装apoc插件 http://neo4j.com.cn/topic/59c27adf1f16d3b94d3274c6    
**neo4j维修服务部分导出csv，cypher语句：**  
match(n:实例节点:维修服务)-[r]->(m:实例节点:维修服务)   
where not n:智能头盔 and not m:智能头盔   
with collect(distinct n) as heads, collect(distinct m) as tails, collect(r) as rels   
CALL apoc.export.csv.data(heads+tails, rels, "ISKG_maintain.csv", {})   
YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data   
RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data 注：这个cypher语句导出的数据，因为(h, r, t) (t, x, y)，t可能出现两次，数据处理时实体要去重。 

#### 补充论文：   
https://weizhixiaoyi.com/paper.html

#### thunlp的repo：  
https://github.com/thunlp/OpenKE

#### 基于图谱embedding的问答：
https://github.com/xhuang31/KEQA_WSDM19

#### 腾讯文档：  
图谱embedding文档  
https://docs.qq.com/doc/DQm1DQXh0bGZXSEVG  
图谱问答文档  
https://docs.qq.com/doc/DQlZDWld3Vk1yTGF0
