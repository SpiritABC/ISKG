import numpy as np

# getID: use train/valid/test.txt to create entity2id/relation2id.txt, making entity&relation unique
# train/valid/test_marked.txt just copy train/valid/test.txt
def getID(folder='data/ISKG/'):
    lstEnts = {}
    lstRels = {}
    with open(folder + 'train.txt') as f, open(folder + 'train_marked.txt', 'w') as f2:
        count = 0
        for line in f:
            line = line.strip().split()
            line = [i.strip() for i in line]
            # print(line[0], line[1], line[2])
            if line[0] not in lstEnts:
                lstEnts[line[0]] = len(lstEnts) # so that entity unique id: 0, 1, 2, ..., n
            if line[1] not in lstRels:
                lstRels[line[1]] = len(lstRels) # so that relation unique id: 0, 1, 2, ..., m
            if line[2] not in lstEnts:
                lstEnts[line[2]] = len(lstEnts)
            count += 1
            f2.write(str(line[0]) + '\t' + str(line[1]) +
                     '\t' + str(line[2]) + '\n')
        print("Size of train_marked set set ", count)

    with open(folder + 'valid.txt') as f, open(folder + 'valid_marked.txt', 'w') as f2:
        count = 0
        for line in f:
            line = line.strip().split()
            line = [i.strip() for i in line]
            # print(line[0], line[1], line[2])
            if line[0] not in lstEnts:
                lstEnts[line[0]] = len(lstEnts)
            if line[1] not in lstRels:
                lstRels[line[1]] = len(lstRels)
            if line[2] not in lstEnts:
                lstEnts[line[2]] = len(lstEnts)
            count += 1
            f2.write(str(line[0]) + '\t' + str(line[1]) +
                     '\t' + str(line[2]) + '\n')
        print("Size of VALID_marked set set ", count)

    with open(folder + 'test.txt') as f, open(folder + 'test_marked.txt', 'w') as f2:
        count = 0
        for line in f:
            line = line.strip().split()
            line = [i.strip() for i in line]
            # print(line[0], line[1], line[2])
            if line[0] not in lstEnts:
                lstEnts[line[0]] = len(lstEnts)
            if line[1] not in lstRels:
                lstRels[line[1]] = len(lstRels)
            if line[2] not in lstEnts:
                lstEnts[line[2]] = len(lstEnts)
            count += 1
            f2.write(str(line[0]) + '\t' + str(line[1]) +
                     '\t' + str(line[2]) + '\n')
        print("Size of test_marked set set ", count)

    wri = open(folder + 'entity2id.txt', 'w')
    for entity in lstEnts:
        wri.write(entity + '\t' + str(lstEnts[entity]))
        wri.write('\n')
    wri.close()

    wri = open(folder + 'relation2id.txt', 'w')
    for entity in lstRels:
        wri.write(entity + '\t' + str(lstRels[entity]))
        wri.write('\n')
    wri.close()


folder='data/ISKG/'
getID(folder)
