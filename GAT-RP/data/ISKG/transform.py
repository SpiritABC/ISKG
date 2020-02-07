
import pandas as pd

# convert train2id/test2id/valid2id to original triple train/valid/test (before re-encoding)
entity = pd.read_csv('entity2id.txt', header=None, sep='\t')
entity.columns = ['name', 'id']
relation = pd.read_csv('relation2id.txt', header=None, encoding='gbk', sep='\t')
relation.columns = ['name', 'id']
entity_dict = dict(zip(entity['id'], entity['name']))
relation_dict = dict(zip(relation['id'], relation['name']))

file_list = ['train2id.txt', 'test2id.txt', 'valid2id.txt']
for i in file_list:

    df = pd.read_csv(i, sep='\t', header=None)
    df.columns = ['e1', 'e2', 'r']
    df['e1'] = df['e1'].map(entity_dict).astype(int)
    df['e2'] = df['e2'].map(entity_dict).astype(int)
    df['r'] = df['r'].map(relation_dict)
    df = df[['e1', 'r', 'e2']]
    df.to_csv(i.replace('2id', ''), index=False, header=None, sep='\t')