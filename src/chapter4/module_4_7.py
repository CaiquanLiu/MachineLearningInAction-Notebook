# coding:utf-8
'''
Created on 2017/11/24 上午8:48

@author: liucaiquan
'''
'''
示例:使用朴素贝叶斯来发现地域相关的用词 
(1) 收 集 数 据 :从尺83源收集内容，这里需要对尺88源构建一个接口。 
(2)准备数据:将文本文件解析成词条向量。 
(3)分析数据:检查词条确保解析的正确性。 
(4)训练算法:使用我们之前建立的trainNB0()函数。 
(5)测试算法:观察错误率，确保分类器可用。可以修改切分程序，以降低错误率，提高分类结果。 
(6)使用算法:构建一个完整的程序，封装所有内容。给定两个尺88源，该程序会显示最常用的公共词。
'''


# import feedparser
# ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# print 'type= {}'.format(type(ny))
# print 'ny={}'.format(ny)

def calcMostFreq(vocabList, fullText):
    '''
    高词频词语检测
    :param vocabList: 词表
    :param fullText:  所有文本
    :return:
    '''
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token] = fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


from module_4_6 import textParse
from module_4_5 import createVocabList
from module_4_5 import bagOfWords2VecMN
from module_4_5 import trainNB0
from module_4_5 import classifyNB
from numpy import array
import random


def localWords(feed1, feed0):
    '''
    使用RSS进行朴素贝叶斯测试
    :param feed1: RSS1样本
    :param feed0: RSS2样本
    :return: 词表，p0V, p1V
    '''
    import feedparser
    docList = [];
    classList = [];
    fullText = []
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(i)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList, fullText)
    for pairW in top30Words:
        if pairW[0] in vocabList:
            vocabList.remove(pairW[0])
    trainingSet = range(2 * minLen);
    testSet = []
    # print 'trainingSet={}'.format(2*minLen)
    for i in range(20):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount) / len(testSet)
    return vocabList, p0V, p1V


# import feedparser
# ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# # print 'ny={}'.format(ny)
# sf=feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
# # print 'sf={}'.format(sf)
#
# # localWords(ny,sf)

def getTopWords(ny, sf):
    '''
    高频词统计
    :param ny: RSS1
    :param sf: RSS2
    :return: 打印输出
    '''
    import operator
    vocabList, p0V, p1V = localWords(ny, sf)
    topNY = [];
    topSF = []
    for i in range(len(p0V)):
        if p0V[i] > -6.0: topSF.append((vocabList[i], p0V[i]))
        if p1V[i] > -6.0: topNY.append((vocabList[i], p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY **"
    for item in sortedNY:
        print item[0]


import feedparser

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
print 'ny={}'.format(ny)
sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
print 'sf={}'.format(sf)

getTopWords(ny, sf)
