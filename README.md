# 《机器学习实战》学习笔记

《Machine Learning in Action》的中文译本名为《机器学习实战》。本项目以实际运行书中的测试用例，并添加相应的注释作为学习笔记。

## 运行环境
* MacBook Pro(Mac OS 10.12.6)
* Python 2.7(Anaconda)

# 当前进度
## 第二章 K-临近算法
* 2-1 k-近邻算法概述（module_2_1）

        def createDataSet():
            '''
            创建数据集
            :return: 样本特征集合，样本标签集合
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
* 2-2 示例：使用k-近邻算法改进约会网站的配对效果(module_2_2)

        def file2matrix(filename):
            '''
            将文本记录到转换NumPy的解析程序
            :param filename:
            :return:文件向量
            '''
    
        def autoNorm(dataSet):
            '''
            归一化特征值
            :param dataSet:
            :return: 归一化样本集合，范围，最小值
            '''
    
        def datingClassTest():
            '''
            分类器针对约会网站的测试代码
            :return:打印输出
            '''
    
        def classifyPerson():
            '''
            约会网站预测函数
            :return: 打印输出
            '''
* 2-3 示例：手写识别系统（module_2_3）

        def img2vector(filename):
            '''
            图像向量化
            :param filename: 图像文件
            :return:向量化结果
            '''
    
        def handwritingClassTest():
            '''
            手写数字识别系统的测试代码
            :return: 打印输出
            '''

## 第三章 决策树
* 3-1 决策树的构造(module_3_1)
        def calcShannonEnt(dataSet):
            '''
            计算给定数据集的香农熵
            :param dataSet: 测试数据集
            :return: 数据集香浓值
            '''
        
        def createDataSet():
            '''
            自定义数据集
            :return: 自定义的数据集
            '''
        
        def splitDataSet(dataSet, axis, value):
            '''
            按照给定特征划分数据集
            :param dataSet: 需要划分的数据集
            :param axis:划分数据集的特征
            :param value:特征的返回值
            :return: 划分后的数据集
            '''
    
        def chooseBestFeatureToSplit(dataSet):
            '''
            选择最好的数据集划分方式
            :param dataSet: 待划分数据集
            :return: 选择的特征
            '''
    
        def majorityCnt(classList):
            '''
            出现次数最多的分类名称
            :param classList: 分类
            :return: 分类名称
            '''
    
        def createTree(dataSet, labels):
            '''
            创建树的函数代码
            :param dataSet: 数据集
            :param labels: 标签
            :return: 决策树
            '''
* 3-2 在 Python中使用Matplotlib注解绘制树形图(module_3_2)

        def plotNode(nodeTxt, centerPt, parentPt, nodeType):
            '''
            决策树节点绘制
            :param nodeTxt:节点内容
            :param centerPt:root节点
            :param parentPt:父节点
            :param nodeType:节点类型
            :return:
            '''

        def createPlot():
            '''
            测试用例，绘制两个节点
            :return:
            '''
            
        def getNumLeafs(myTree):
            '''
            获得叶子节点的个数
            :param myTree: 决策树
            :return:
            '''
    
        def getTreeDepth(myTree):
            '''
            决策树深度
            :param myTree:决策树
            :return:
            '''
            
        def retrieveTree(i):
            '''
            获取决策树样例
            :param i:决策树索引
            :return:
            '''
    
        def plotMidText(cntrPt, parentPt, txtString):
            '''
            决策树父子节点之间的关系绘制
            :param cntrPt: 决策树节点
            :param parentPt: 父节点
            :param txtString: 节点描述
            :return:
            '''
            
        def plotTree(myTree, parentPt, nodeTxt):
            '''
            决策树递归绘制
            :param myTree:待绘制决策树
            :param parentPt: 父节点
            :param nodeTxt: 节点描述
            :return:
            '''
    
        def createPlot(inTree):
            '''
            完整决策树绘制
            :param inTree: 决策树
            :return:
            '''
* 3-3 测试和存储分类器(module_3_3) 