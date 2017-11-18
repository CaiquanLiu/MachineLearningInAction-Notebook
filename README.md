#《机器学习实战》学习笔记

《Machine Learning in Action》的中文译本名为《机器学习实战》.本项目以实际运行书中的测试用例，并添加相应的注释作为学习笔记。

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