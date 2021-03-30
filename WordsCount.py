import MyNLP as NLP
import datetime

infoSet = []
info_count = {}
wordsSet = {}

#数据集生成
def InfoSet_Comput(data):
    for i in data:
        infoSet.append(NLP.Info_kw(i[0], i[1], i[2], i[3]))

    
    for i in infoSet:
        for j in i.KW:
            if j in info_count:
                info_count[j] += 1
            else:
                info_count[j] = 1
            if wordsSet.get(j, -1) == -1:
                wordsSet[j] = []
            wordsSet[j].append(i)

    temp_CountList= sorted(info_count.items(), key = lambda t : t[1], reverse = True)

    info_count.clear()
    for item in temp_CountList:
        info_count[item[0]] = item[1]

#获取总排名前十的热词
def get_TopTenInfo():
    index = 0
    res = {}
    for i in info_count.items():
        res[i[0]] = i[1]
        index += 1
        if index >= 10:
            break

    return res

#获取某个关键词当天及前30天出现的频度
def get_30DaysInfo(word):
    date = datetime.date.today()
    dic = {}
    for i in range(0, 31):                 #当天的前0到30天
        dic[i] = 0
    set = wordsSet[word]

    for item in set:
        sub = (date.__sub__(item.time.date())).days
        if sub <= 30:
            dic[sub] += 1
    return dic

#获取某个关键词当月及前12月出现的频度
def get_12MonthsInfo(word):
    date = datetime.date.today()
    dic = {}
    for i in range(0, 13):                  #当月的前0到12个月
        dic[i] = 0
    set = wordsSet[word]

    for item in set:
        sub = date.month - item.time.date().month + (date.year - item.time.date().year) * 12
        if sub <= 12:
            dic[sub] += 1
    return dic

#获取某个关键词当年及前10年出现的频度
def get_10YearsInfo(word):
    date = datetime.date.today()
    dic = {}
    for i in range(0, 11):                  #当年的前0到10年
        dic[i] = 0
    set = wordsSet[word]

    for item in set:
        sub = date.year - item.time.date().year
        if sub <= 10:
            dic[sub] += 1
    return dic