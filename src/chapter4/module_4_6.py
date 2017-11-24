# coding:utf-8
'''
Created on 2017/11/23 上午9:19

@author: liucaiquan
'''
'''
示例：使用朴素贝叶斯对电子邮件进行分类
(1)收集数据:提供文本文件
(2)准备数据:将文本文件解析成词条向量
(3)分析数据:检查词条确保解析的正确性
(4)训练算法:使用我们之前建立的trainNB0()函数。
(5)测试算法:使用clasSifyNB()，并且构建一个新的测试函数来计算文档集的错误率。 
(6)使用算法:构建一个完整的程序对一组文档进行分类，将错分的文档输出到屏幕上。
'''


# mySent='This book is the best book on Python or M.L. I have ever laid W eyes upon.'
# # print mySent.split()
#
# import re
# regEx = re.compile('\\W*')
# listOfTokens = regEx.split(mySent)
# # print listOfTokens
#
# [tok.lower() for tok in listOfTokens if len(tok) > 0]

# import re
# emailText = open('email/ham/6.txt').read()
# regEx = re.compile('\\W*')
# listOfTokens=regEx.split(emailText)
# print listOfTokens

def textParse(bigString):
    '''
    分词
    :param bigString: 文本内容
    :return:
    '''
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


from module_4_5 import createVocabList
from module_4_5 import setOfWords2Vec
from module_4_5 import trainNB0
from module_4_5 import classifyNB
from numpy import array
import random


def spamTest():
    '''
    使用朴素贝叶斯进行邮件分类测试
    :return:
    '''
    docList = [];
    classList = [];
    fullText = []
    for i in range(1, 26):
        # content=open('email/spam/%d.txt' % i).read()
        # print 'type= {}'.format(type(content))
        # print 'content= {}'.format(content)

        wordList = textParse(open('email/spam/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])

    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    pOV, plV, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0

    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), pOV, plV, pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ', float(errorCount) / len(testSet)

# spamTest()
