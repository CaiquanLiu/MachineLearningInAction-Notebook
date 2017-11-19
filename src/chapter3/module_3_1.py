# coding:utf-8
'''
Created on 2017/11/18 下午12:01

@author: liucaiquan
'''
from math import log


def calcShannonEnt(dataSet):
    '''
    计算给定数据集的香农熵
    :param dataSet: 测试数据集
    :return: 数据集香浓值
    '''
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def createDataSet():
    '''
    自定义数据集
    :return: 自定义的数据集
    '''
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]

    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# myDat, labels = createDataSet()
# print calcShannonEnt(myDat)


def splitDataSet(dataSet, axis, value):
    '''
    按照给定特征划分数据集
    :param dataSet: 需要划分的数据集
    :param axis:划分数据集的特征
    :param value:特征的返回值
    :return: 划分后的数据集
    '''
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)

    return retDataSet


# myDat, labels = createDataSet()
# print splitDataSet(myDat, 0, 1)

def chooseBestFeatureToSplit(dataSet):
    '''
    选择最好的数据集划分方式
    :param dataSet: 待划分数据集
    :return: 选择的特征
    '''
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


# myDat, labels = createDataSet()
# print labels
# print chooseBestFeatureToSplit(myDat)

import operator


def majorityCnt(classList):
    '''
    出现次数最多的分类名称
    :param classList: 分类
    :return: 分类名称
    '''
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
            classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    '''
    创建树的函数代码
    :param dataSet: 数据集
    :param labels: 标签
    :return: 决策树
    '''
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myDat, labels = createDataSet()
myTree = createTree(myDat, labels)
print myTree
