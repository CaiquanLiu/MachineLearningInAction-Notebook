# coding:utf-8
'''
Created on 2017/11/17 上午8:21

@author: liucaiquan
'''
'''
示例:在约会网站上使用&近邻算法
(1)收集数据:提供文本文件。
(2)_准备数据: 使用?沖 00解析文本文件。 
(3)分析数据:使用河3中10«化画二维扩散图。 
(4)训练算法:此步驟不适用于卜近邻算法。 
(5)测试算法:使用海伦提供的部分数据作为测试样本。
(6)使用算法:产生简单的命令行程序，然后海伦可以输入一些特征数据以判断对方是否为自己喜欢的类型。
'''
from numpy import *
import operator

import module_2_1


def file2matrix(filename):
    '''
    将文本记录到转换NumPy的解析程序
    :param filename:
    :return:
    '''
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        # print 'listFromLine= {}'.format(listFromLine)
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


datingDataMat, datingLabels = file2matrix('data/datingTestSet2.txt')


# print datingDataMat
# print datingLabels

# import matplotlib
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # print datingDataMat[:,1]
# # ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
# plt.show()

def autoNorm(dataSet):
    '''
    归一化特征值
    :param dataSet:
    :return:
    '''
    minVals = dataSet.min(0)
    # print 'minVals={}'.format(minVals)

    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


normMat, ranges, minVals = autoNorm(datingDataMat)
print 'normMat={}'.format(normMat)
