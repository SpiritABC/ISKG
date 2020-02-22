from py2neo import *
import pandas as pd
import types

graph = Graph("http://localhost:11003", username='name', password="741358")

# resCur = graph.run('match(n:实例节点:维修服务) \
#                     with n, size((n)-[]->()) as outDegree, size((n)<-[]-()) as inDegree \
#                     where not n:智能头盔 \
#                     return inDegree, outDegree')

resCur = graph.run('match(n:客户:实例节点:维修服务) \
                    with n, size((n)-[]->()) as outDegree, size((n)<-[]-()) as inDegree \
                    return n.客户名称, inDegree, outDegree')
d = resCur.to_data_frame()
print(len(d))


# delete duplicate nodes

# resCur = graph.run('match(n:挖掘机:维修服务:实例节点) \
#                     with n.机号 as jihao, count(n.机号) as tot \
#                     where tot > 1 \
#                     return jihao, tot')
# intL = []
# strL = []
# for dic in l:
#     if isinstance(dic['jihao'], int):
#         intL.append(dic['jihao'])
#     else:
#         strL.append(dic['jihao'])

# print(len(intL)+len(strL))

# wajuejiDel = resCur.to_data_frame()
# print(wajuejiDel.head(20))

# 分成数字和字符串两组

# for n in strL:
#     graph.run('match(n:挖掘机:实例节点:维修服务)-[r]-() \
#                where n.机号="'+n+ \
#                '" delete n,r')

# for jh in wajuejiDel['jihao']:
#     print(jh)

# for learning
# m = NodeMatcher(graph)
# n = m.match("概念节点").limit(10)
# print(n)
# f = n.first()
# print(f)
# r = list(n)
# print(r)


