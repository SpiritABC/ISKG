import jieba

jieba.load_userdict("./userdict.txt")

text = "机号为DBBG6548的挖掘机在什么地方"
# 精确模式
seg_list = jieba.cut(text, cut_all=False)
print(u"[精确模式]: ", "/ ".join(seg_list))