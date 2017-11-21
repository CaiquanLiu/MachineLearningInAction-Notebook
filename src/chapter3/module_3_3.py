# coding:utf-8
'''
Created on 2017/11/20 上午10:19

@author: liucaiquan
'''

from chapter3.module_3_1 import createDataSet
from chapter3.module_3_2 import retrieveTree


def classify(inputTree, featLabels, testVec):
    '''
    使用决策树的分类函数
    :param inputTree: 决策树
    :param featLabels: 标签
    :param testVec: 待分类样本
    :return:
    '''
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


# myDat, labels = createDataSet()
# print  labels
#
# myTree = retrieveTree(0)
# print myTree
#
# print classify(myTree, labels, [1, 0])
#
# print classify(myTree, labels, [1, 1])

def storeTree(inputTree, filename):
    '''
    使用pickle存储决策树
    :param inputTree: 决策树
    :param filename: 保存文件名
    :return:
    '''
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    '''
    使用pickle恢复决策树
    :param filename: 文件名
    :return:
    '''
    import pickle
    fr = open(filename)
    return pickle.load(fr)


# myTree = retrieveTree(0)
# storeTree(myTree, 'classifierStorage.txt')
# print grabTree('classifierStorage.txt')
