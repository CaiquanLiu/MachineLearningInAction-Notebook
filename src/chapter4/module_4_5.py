# coding:utf-8
'''
Created on 2017/11/21 下午4:16

@author: liucaiquan
'''


def loadDataSet():
    '''
    创建数据集
    :return: 数据集，分类
    '''
    postingList = [['my', 'dog', 'has', 'flea', \
                    'problems', 'help', 'please'], ['maybe', 'not', 'take', 'him', \
                                                    'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', \
                    'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', \
                    'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog' 'food', 'stupid']]

    classVec = [0, 1, 0, 1, 0, 1]  # 1 代表侮辱性文字，0代表正常言论
    return postingList, classVec


def createVocabList(dataSet):
    '''
    创建词表
    :param dataSet:
    :return:
    '''
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    '''
    输入数据向量化
    :param vocabList: 输入文本
    :param inputSet: 词表
    :return:
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word:%s is not in my Vocabulary!" % word

    return returnVec


# listOPosts, listClasses = loadDataSet()
# myVocabList = createVocabList(listOPosts)
# print myVocabList
# print setOfWords2Vec(myVocabList, listOPosts[0])

from numpy import *


def trainNB0(trainMatrix, trainCategory):
    '''
    朴素贝叶斯关键参数计算
    :param trainMatrix: 已词集向量化的数据集
    :param trainCategory: 分类结果
    :return: P(w|A), P(w|B), P(A)
    '''
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # p0Num = zeros(numWords)
    # p1Num = zeros(numWords)
    # p0Denom = 0.0
    # p1Denom = 0.0

    # 分类器修复
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])

    # p1Vect = p1Num / p1Denom
    # p0Vect = p0Num / p0Denom

    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive


# listOPosts, listClasses = loadDataSet()
# myVocabList = createVocabList(listOPosts)
# trainMat = []  # 向量化后的文章样本
# for postinDoc in listOPosts:
#     trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

# print 'trainMat={}'.format(trainMat)
# p0V, p1V, pAb = trainNB0(trainMat, listClasses)
# print 'p0V={}'.format(p0V)
# print 'p1V={}'.format(p1V)
# print 'pAb={}'.format(pAb)

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    '''
    朴素贝叶斯分类计算
    :param vec2Classify: 已词集向量化的数据集
    :param p0Vec: P(w|A)
    :param p1Vec: P(w|B)
    :param pClass1: P(A)
    :return:
    '''
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    '''
    自定义数据集分类测试
    :return:
    '''
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb)


# testingNB()

def bagOfWords2VecMN(vocabList, inputSet):
    '''
    朴素贝叶斯词袋模型
    :param vocabList: 词表
    :param inputSet: 待向量化原始样本
    :return:
    '''
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
