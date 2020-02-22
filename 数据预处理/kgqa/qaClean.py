import pandas as pd
from py2neo import *
import types

# _path = 'C:/Users/lxabc/Desktop/QAdata/'
# t = pd.read_csv(_path+'ISKG_maintain.csv', sep=',', encoding='utf-8', low_memory=False)
# # print(len(t[t['type']=='挖掘机'])) # 挖掘机个数
# # kehu_pl = t[(t['联系人姓名'].notnull) and (t['联系人姓名'] != "")]
# kehu_pl = t[t['_labels']==':实例节点:客户:维修服务']
# kehu_duliID = kehu_pl.drop_duplicates(subset=['_id'])
# kehu_duliID = kehu_duliID[['_id', '_labels', '客户名称', '客户号']]
# print(len(kehu_duliID))
# kehu_u = kehu_duliID['客户名称'].str.cat(kehu_duliID['客户号'].str[-4:])
# # 添加为新的列
# kehu_duliID['name'] = kehu_u
# kehu_du = kehu_duliID[kehu_duliID['name'].duplicated(keep=False)]
# print(kehu_du)
#
# kehu_uv = list(kehu_u.unique())
# # print(kehu_pl['姓名'].value_counts())
# print(len(kehu_uv))

# 是否有空值
# kehu_null = kehu_u[kehu_u.isnull().values==True]
# print(kehu_null)
# print(kehu_u)


# 查neo4j验证
graph = Graph("http://localhost:11003", username='name', password="741358")

resCur = graph.run('match(n:方案:实例节点:维修服务) \
                    with id(n) as id, n.作业名称 as name, n.作业卡编号 as num\
                    return id, name, num')
d = resCur.to_data_frame()
d['num'] = d['num'].apply(str)
d['name'] = d['name'].apply(str)
# 联系人如果为空 删除
print(len(d))
# 删除联系人姓名为空的联系人
# nulldel = d[d['name']==""]
# print(len(nulldel))
# for id in list(nulldel['id']):
#     graph.run('match(n:联系人:实例节点:维修服务)-[r]-() \
#                where id(n)='+str(id)+' \
#                delete n,r')
lingjian = d['name'].str.cat(d['num'].str[-4:])
d['lingjian'] = lingjian
lingjian_de = d[d['lingjian'].duplicated(keep=False)]
lingjian_uv = list(d['lingjian'].unique())
# lj_deuv = list(lingjian_de['lingjian'].unique())
print(len(lingjian_uv))
print(len(lingjian_de))
print(lingjian_de)
print(lingjian)
# print(len(lxr_deuv))
# 删除重复的联系人，联系人姓名、联系人电话都相同,共300个
# for id in list(lxr_de['id']):
#     graph.run('match(n:联系人:实例节点:维修服务)-[r]-() \
#                where id(n)='+str(id)+' \
#                delete n,r')


# # print(len(t[t['type']=='挖掘机'])) # 挖掘机个数
# kehu_pl = t[(t['客户名称'].notnull) and (t['客户名称'] != "")]
# # kehu_pl = t[t['_labels']==':实例节点:客户:维修服务']
# #kehu_n = kehu_pl['客户名称']
# #kehu_nv = list(kehu_n.unique())
# kehu_u = kehu_pl['客户名称'].str.cat(kehu_pl['客户号'].str[10:])
# kehu_uv = list(kehu_u.unique())
# print(len(kehu_uv))
# print(kehu_uv)






# 删除服务人员使用车的代码
# resCur = graph.run('match(n:服务人员使用车:实例节点:维修服务) \
#                     with id(n) as id, n.车牌 as chepai\
#                     return id, chepai')
# d = resCur.to_data_frame()
# d['chepai'] = d['chepai'].apply(str)
# che_de = d[d['chepai'].duplicated(keep='last')]
# # print(list(che_de['id']))
# for id in list(che_de['id']):
#     graph.run('match(n:服务人员使用车:实例节点:维修服务)-[r]-() \
#                where id(n)='+str(id)+' \
#                delete n,r')


# 联系人清洗代码：
# resCur = graph.run('match(n:联系人:实例节点:维修服务) \
#                     with id(n) as id, n.联系人姓名 as name, n.联系人电话 as tel\
#                     return id, name, tel')
# d = resCur.to_data_frame()
# d['tel'] = d['tel'].apply(str)
# d['name'] = d['name'].apply(str)
# # 联系人如果为空 删除
# print(len(d))
# # 删除联系人姓名为空的联系人
# # nulldel = d[d['name']==""]
# # print(len(nulldel))
# # for id in list(nulldel['id']):
# #     graph.run('match(n:联系人:实例节点:维修服务)-[r]-() \
# #                where id(n)='+str(id)+' \
# #                delete n,r')
# lianxiren = d['name'].str.cat(d['tel'].str[-4:])
# d['mingcheng'] = lianxiren
# lxr_de = d[d['mingcheng'].duplicated(keep='first')]
# lxr_uv = list(d['mingcheng'].unique())
# # lxr_deuv = list(lxr_de['mingcheng'].unique())
# print(len(lxr_uv))
# print(len(lxr_de))
# print(lxr_de)
# # print(len(lxr_deuv))
# # 删除重复的联系人，联系人姓名、联系人电话都相同,共300个
# # for id in list(lxr_de['id']):
# #     graph.run('match(n:联系人:实例节点:维修服务)-[r]-() \
# #                where id(n)='+str(id)+' \
# #                delete n,r')