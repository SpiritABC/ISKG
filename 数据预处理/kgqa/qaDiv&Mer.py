import pandas as pd
import numpy as np

# 1. 读取qaset.txt, 判断有没有空值
# 2. 按头实体概念分成若干个txt来标注

# _path = 'C:/Users/lxabc/Desktop/QAdata'

# tri = pd.read_csv(_path+'qaset.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on'],
#                   encoding='utf-8' ,dtype=np.str)
# # cols = list(tri)
# # for col in cols:
# #     naidx = tri.index[tri[col].isna()]
# #     print(naidx)
# stype = tri['sn'].unique()
# print(stype)
# for type in stype:
#     data = tri[tri['sn'].isin([type])]
#     data.to_csv(_path + 'QAname/'+type+'.txt', sep='\t', header=False, index=False, encoding='utf_8_sig')

_path = 'C:/Users/lxabc/Desktop/QAdata/QAnoted/'

ywqt = pd.read_csv(_path+'业务前台noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
ccry = pd.read_csv(_path+'仓储人员noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
ccd = pd.read_csv(_path+'出库单noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
kh = pd.read_csv(_path+'客户noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
gd = pd.read_csv(_path+'工单noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
wjj = pd.read_csv(_path+'挖掘机noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
fwpg = pd.read_csv(_path+'服务派工noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
jxfl = pd.read_csv(_path+'机型分类noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
xcfwry = pd.read_csv(_path+'现场服务人员noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
bj = pd.read_csv(_path+'部件noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
zd = pd.read_csv(_path+'驻点noted.txt', sep='\t', header=None, names=['s', 'p', 'o', 'sn', 'on', 'q'],
                  encoding='utf-8' ,dtype=np.str)
tri_n = pd.concat([ywqt, ccry, ccd, kh, gd, wjj, fwpg, jxfl, xcfwry, bj, zd])
print(len(tri_n))
tri_n.to_csv(_path+'qaSetNoted.txt', sep='\t', header=False,index=False, encoding='utf_8_sig')