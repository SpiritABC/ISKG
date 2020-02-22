import pandas as pd
import numpy as np

# 1. 读取entity2id/relation2id/ISKG.csv/triple2id
# 2. triple2id调整为(s, p, o), entity2id/relation2id调整字典顺序{编号：_id}
# 3. (s, p, o)中p替换为名称，s/o替换为_id
# 4. s/o每个id与csv的"_id"匹配，得到csv的一行简称line
# 5. 取line的type属性判断实体类型，根据实体类型使用相应规则选择属性作为名称，保存line对应的type
# 6. 保存格式为 s p o stype otype
_path = 'C:/Users/lxabc/Desktop/QAdata/'
# 1
csv = pd.read_csv(_path+'ISKG.csv', sep=',', dtype=np.str, encoding='utf-8', low_memory=False)
tri = pd.read_csv(_path+'triple2id.txt', sep='\t', header=None, names=['head', 'tail', 'rel'], encoding='utf-8'
                ,dtype=np.str, skiprows=1) # skiprows, skip前n行，或者[0, n...]skip第几行
e2id = pd.read_csv(_path+'entity2id.txt', sep='\t', header=None, names=['_id', 'idx'], encoding='utf-8'
                ,dtype=np.str, skiprows=1)
r2id = pd.read_csv(_path+'relation2id.txt', sep='\t', header=None, names=['rname', 'idx'],
                   encoding='utf-8-sig', dtype=np.str, skiprows=1)
# 2
cols=list(tri)
print(cols)
cols.insert(1, cols.pop(cols.index('rel')))
print(cols)
tri = tri.loc[:, cols]
print(tri.head(3))
# 3
pdic = r2id.set_index('idx').to_dict()['rname']
tri['rel'] = tri['rel'].apply(lambda x: pdic[x])
edic = e2id.set_index('idx').to_dict()['_id']
tri['head'] = tri['head'].apply(lambda x: edic[x])
tri['tail'] = tri['tail'].apply(lambda x: edic[x])
print(tri.head(3))
# 4 and 5
_idx = csv['_start'].first_valid_index()
csveti = csv.iloc[:_idx, :]  # 用来检索的csv实体集
csveti = csveti.drop_duplicates(subset=['_id']) # 去掉csv中重复行
print(len(csveti))
csveti = csveti[['_id', 'type', 'value', '机号', '客户名称','客户号','工单号','联系人姓名','联系人电话'
        ,'出库单编号','派工单编号','作业名称','作业卡编号','姓名','类型号','名称','车牌']]# 只保留需要用的列
# csveti = csveti.astype(pd.StringDtype)
tri['htype']=None
tri['ttype']=None
# tri = tri.astype(str)
print(tri.head(3))
print(csveti.head(3))

def strim(num, type):
    if num==num and type in ['客户', '联系人', '方案']:
        return num[-4:]
    elif num==num and type=='零件':
        return num[-6:]
    else:
        return ""

def id2name(id, col='head'):  # 供apply使用, 传入x, x找到idx,idx对应的htype、ttype赋值
    line = csveti[csveti['_id'] == id]  # 找到id匹配的行

    line = line.iloc[0,:] # dataframe to series
    type = line['type']
    if type in ['部件', '客户类型', '客户等级', '吨级', '质保状态', '当前所在地区', '工作种类',
            '品牌', '作业形态', '机型', '故障描述', '服务区', '当前工单状态', '现场服务人员', '机型分类']:
        return line['value'], type
    elif type == '挖掘机':
        return line['机号'], type
    elif type == '客户':
        return line['客户名称']+strim(line['客户号'], type), type # 使用str cat可以防止值为nan的情况
    elif type == '工单':
        return line['工单号'], type
    elif type == '联系人':
        return line['联系人姓名']+strim(line['联系人电话'], type), type
    elif type == '出库单':
        return line['出库单编号'], type
    elif type == '服务派工':
        return line['派工单编号'], type
    elif type == '方案':
        return line['作业名称']+strim(line['作业卡编号'], type), type
    elif type == '业务前台':
        return line['姓名'], type
    elif type == '零件':
        return line['名称']+strim(line['类型号'], type), type
    elif type == '仓储人员':
        return line['姓名'], type
    elif type == '驻点':
        return line['名称'], type
    elif type == '服务人员使用车':
        return line['车牌'], type
    else:
        return None, None

# zy = csveti[csveti['作业名称'].notna()]  # nan

for idx, row in tri.iterrows():
    row['head'], row['htype'] = id2name(row['head'])
    row['tail'], row['ttype'] = id2name(row['tail'])

print(tri.head(5))

# 6
tri.to_csv(_path+'qaset.txt', sep='\t', header=False,index=False, encoding='utf_8_sig')

# naidx = tri.index[tri.apply(np.isnan)]
# print(naidx)

# print("bug here: \n")
# bug = csveti[csveti['_id']=='112846']
# print(bug['作业名称'])
# print(bug['作业卡编号'])
#
# rv = bug['作业名称'].item()
# bv = bug['作业卡编号'].item()
# print(rv)
# print(bv)
# if bv == bv:  # 这种办法判断nan是最有效的，其他方法都只能用于某几种类型的数据
#     print("find nan")