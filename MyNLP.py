import pkuseg
import datetime

#加载词性标记、字典、停用词词库、无关词词库
tags = ['n', 'v', 'a']#, 'd'
lexicon = []
stopwords = []
irrelevantwords = []

path = "C:\\Users\\PC\\.pkuseg\\"
f = open(path + "lexicon.txt", "r", encoding = "utf-8")
for line in f:
    lexicon.append(line[:-1])
f.close()
f = open(path + "stopwords.txt", "r", encoding = "utf-8")
for line in f:
    stopwords.append(line[:-1])
f.close()
f = open(path + "IrrelevantWords.txt", "r", encoding = "utf-8")
for line in f:
    irrelevantwords.append(line[:-1])
f.close()

#加载分词器
seg = pkuseg.pkuseg(model_name = "news", user_dict = lexicon, postag = True)

#信息-关键词 结构体
class Info_kw:
    def __init__(self, href, text, time, _from):
        self.href = href
        self.text = text
        self._from = _from
        self.KW = []
        self.NLP()
        time = time.split(" ")[0]
        if time[4] == "-":
            self.time = datetime.datetime.strptime(time, "%Y-%m-%d")
        elif time[4] == "/":
            self.time = datetime.datetime.strptime(time, "%Y/%m/%d")
        elif time[4] == "年":
            self.time = datetime.datetime.strptime(time, "%Y年%m月%d日")


    def NLP(self):
        #分词
        rsts = seg.cut(self.text)

        #去重
        self.temp = []
        for i in rsts:
            if not i[0] in self.temp and i[1] in tags:
                self.temp.append(i[0])

        #去停用词，去无关词
        for i in self.temp:
            if i not in stopwords and i not in irrelevantwords:
                self.KW.append(i)

    def getKW(self):
        return self.KW

