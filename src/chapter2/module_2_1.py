# coding:utf-8
'''
Created on 2017/11/16 上午9:00

@author: liucaiquan
'''
'''
k-近邻算法的一般流程 
(1)收集数据:可以使用任何方法。
(2)准备数据:距离计算所需要的数值，最好是结构化的数据格式。 (3)分析数据:可以使用任何方法。
(4)训练算法:此步驟不适用于1 近邻算法。
(5)测试算法:计算错误率。 (6)使用算法:首先需要输入样本数据和结构化的输出结果，然后运行女-近邻算法判定输
入数据分别属于哪个分类，最后应用对计算出的分类执行后续的处理。
'''
from numpy import *
import operator


def createDataSet():
    '''
    创建数据集
    :return: 样本特征集合，样本标签集合
    '''
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# group, labels = createDataSet()
# print 'group= {}'.format(group)
# print 'labels={}'.format(labels)
# print 'group.shape= {}'.format(group.shape)
# print group.shape[0]

'''
对未知类别属性的数据集中的每个点依次执行以下操作: 
(1)计算已知类别数据集中的点与当前点之间的距离; 
(2)按照距离递增次序排序; 
(3)选取与当前点距离最小的走个点; 
(4)确定前灸个点所在类别的出现频率; 
(5)返回前女个点出现频率最高的类别作为当前点的预测分类。
'''


def classify0(inX, dataSet, labels, k):
    '''
    K临近实现
    :param inX: 待分类样本
    :param dataSet:训练样本特征集合
    :param labels:训练样本标签集合
    :param k: K取值
    :return: 类别
    '''
    # 距离计算
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # print 'diffMat= {}'.format(diffMat)

    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # print 'distances= {}'.format(distances)

    sortedDistIndicies = distances.argsort()
    # print 'sortedDistIndicies= {}'.format(sortedDistIndicies)

    classCount = {}

    # 选择距离最小的k个点
    for i in range(k):
        voteILabel = labels[sortedDistIndicies[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# ans = classifyO([0, 0], group, labels, 3)
# print ans
