# coding:utf-8
'''
Created on 2017/11/19 上午11:25

@author: liucaiquan
'''
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle='<-')


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    '''
    决策树节点绘制
    :param nodeTxt:节点内容
    :param centerPt:root节点
    :param parentPt:父节点
    :param nodeType:节点类型
    :return:
    '''
    createPlot.axl.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def createPlot():
    '''
    测试用例，绘制两个节点
    :return:
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.axl = plt.subplot(111, frameon=False)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


# createPlot()

def getNumLeafs(myTree):
    '''
    获得叶子节点的个数
    :param myTree: 决策树
    :return:
    '''
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    '''
    决策树深度
    :param myTree:决策树
    :return:
    '''
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
    if thisDepth > maxDepth:
        maxDepth = thisDepth

    return maxDepth


def retrieveTree(i):
    '''
    获取决策树样例
    :param i:决策树索引
    :return:
    '''
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': \
                                                      {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': \
                                                      {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                   ]
    return listOfTrees[i]


# print retrieveTree(1)
# myTree = retrieveTree(0)
# print getNumLeafs(myTree)
# print getTreeDepth(myTree)

def plotMidText(cntrPt, parentPt, txtString):
    '''
    决策树父子节点之间的关系绘制
    :param cntrPt: 决策树节点
    :param parentPt: 父节点
    :param txtString: 节点描述
    :return:
    '''
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.axl.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    '''
    决策树递归绘制
    :param myTree:待绘制决策树
    :param parentPt: 父节点
    :param nodeTxt: 节点描述
    :return:
    '''
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)

    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
                     cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def createPlot(inTree):
    '''
    完整决策树绘制
    :param inTree: 决策树
    :return:
    '''
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.axl = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()

# myTree = retrieveTree(0)
# createPlot(myTree)
