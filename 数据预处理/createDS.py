import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

# import csv
_path = 'C:/Users/lxabc/Desktop/ISKG/data/input0202_bs/'
t = pd.read_csv(_path+'ISKG_maintain.csv', sep=',', encoding='utf-8', usecols=['_id', '_start', '_end', '_type'], low_memory=False)
t['_id'] = t['_id'].astype(pd.Int32Dtype())
t['_start'] = t['_start'].astype(pd.Int32Dtype())
t['_end'] = t['_end'].astype(pd.Int32Dtype())
print('lines: %d' % t.shape[0])

# split to entites and relations
_idx = t['_start'].first_valid_index()
print('\nrel index start at : %d' % _idx)
entities = t['_id'][:_idx]
triples = t[['_start', '_end', '_type']][_idx:]
print('\nshow entities series: ')
print(entities.head(5))
print('\nshow rels dataframe: ')
print(triples.head(5))

# entities drop duplicates
entities = entities.drop_duplicates()
# print(type(entities)) entities is series
entities = entities.sort_values(ascending=True)
print('\nshow entities series after drop duplicates: ')
print(entities.head(5))

# re-encode entities from 0-n, save as dict
entities.reset_index(drop=True, inplace=True)
ent_dict = entities.to_dict()
ent_dict = dict(zip(ent_dict.values(), ent_dict.keys()))
print('\nshow entities dict after re-encode: ')
print(ent_dict.items())

# re-encode rels
relsLabel = triples['_type'].drop_duplicates()
relsLabel.reset_index(drop=True, inplace=True)
rels_dict = dict(zip(relsLabel.to_dict().values(), relsLabel.to_dict().keys()))
print('\nshow rels dict after re-encode: ')
print(rels_dict.items())

# replace rels token to id
triples['_type'] = triples['_type'].apply(lambda x: rels_dict[x])
print("\nrels id replacement: ")
print(triples.head(5))
print("\nunique rels id: ")
print(triples['_type'].unique())

# replace entities id to new id
triples['_start'] = triples['_start'].apply(lambda x: ent_dict[x])
triples['_end'] = triples['_end'].apply(lambda x: ent_dict[x])
print("\ntriple length: ")
print(triples.shape[0])
print("\ntriples after re-encode: ")
print(triples.head(5))

# save entities/relations/triples encoding
efile = open(_path+'entity2id.txt', 'w')
efile.write(str(len(ent_dict))+'\n')
for k,v in ent_dict.items():
    efile.write(str(k)+'\t'+str(v)+'\n')
efile.close()

rfile = open(_path+'relation2id.txt', 'w')
rfile.write(str(len(rels_dict))+'\n')
for k,v in rels_dict.items():
    rfile.write(str(k)+'\t'+str(v)+'\n')
rfile.close()

tfile = open(_path+'triple2id.txt', 'w')
tfile.write(str(triples.shape[0])+'\n')
tfile.close()
triples.to_csv(_path+'triple2id.txt', sep='\t', header=False,index=False, mode='a')

# split valid and test
t = pd.read_csv(_path+'triple2id.txt', sep='\t', header=None, names=['head', 'tail', 'rel'], encoding='utf-8'
                ,dtype=np.int32, skiprows=1) # skiprows, skip前n行，或者[0, n...]skip第几行

# random_state 可以调整，可以去掉
# iloc是行位置，而loc是dataframe的行index, train_index/test_index返回的是行位置，用iloc
sp = StratifiedShuffleSplit(n_splits = 1,test_size = 0.1,random_state = 0) # 10%
for train_index, test_index in sp.split(t, t['rel']):
    trainds = t.iloc[train_index]
    tvds = t.iloc[test_index]

# rels distribution
print("\ntest/valid rels distribution: ")
print(tvds['rel'].value_counts())

# total triple have entity not in train
# t_ents = trainds['head'].append(trainds['tail']) # 在series中检索会有问题，用unique是准确的
# t_entuni = t_ents.unique()
# t_reluni = trainds['rel'].unique()
trainHeadUni = trainds['head'].unique()
trainTailUni = trainds['tail'].unique()
i = 0
idxlist = []
for idx, row in tvds.iterrows():
    if row['head'] not in trainHeadUni or row['tail'] not in trainTailUni:
        i+=1
        idxlist.append(idx)
print("\ntotal triple have entity not in train: ")
print(i)

# append to train and drop from valid/test
trainds = trainds.append(tvds.loc[idxlist])
tvds = tvds.drop(index=idxlist)

relsdis = tvds['rel'].value_counts()
print("\ntest/valid relation distribution after drop: ")
print(tvds['rel'].value_counts())

if relsdis.empty:
    idx = relsdis[relsdis.values==1].index
    add = tvds.loc[idx]
    tvds = tvds.drop(index=idx)
    print("\nrels 1 index: ")
    print(idx)

trainds = trainds.sample(frac=1).reset_index(drop=True)
tvds = tvds.sample(frac=1).reset_index(drop=True)

# tvds划分valid和test
spt = StratifiedShuffleSplit(n_splits = 1,test_size = 0.5,random_state = 0) # 50% test
for test_index, valid_index in spt.split(tvds, tvds['rel']):
    testds = tvds.iloc[test_index]
    validds = tvds.iloc[valid_index]

# add un-split line to valid
if relsdis.empty:
    validds = validds.append(add)

# save train/valid/test data set
trfile = open(_path+'train2id.txt', 'w')
trfile.write(str(trainds.shape[0])+'\n')
trfile.close()
trainds.to_csv(_path+'train2id.txt', sep='\t', header=False,index=False, mode='a')

vafile = open(_path+'valid2id.txt', 'w')
vafile.write(str(validds.shape[0])+'\n')
vafile.close()
validds.to_csv(_path+'valid2id.txt', sep='\t', header=False,index=False, mode='a')

tsfile = open(_path+'test2id.txt', 'w')
tsfile.write(str(testds.shape[0])+'\n')
tsfile.close()
testds.to_csv(_path+'test2id.txt', sep='\t', header=False,index=False, mode='a')






