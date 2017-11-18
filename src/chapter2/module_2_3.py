# coding:utf-8
'''
Created on 2017/11/18 上午8:57

@author: liucaiquan
'''
'''
示例:使用允-近邻算法的手写识别系统
(1)收集数据:提供文本文件。 
(2)准备数据:编写函数classify0(),将图像格式转换为分类器使用的制格式。 
(3)分析数据:在?5^0^命令提示符中检查数据，确保它符合要求。
(4)训 练 算 法 :此步驟不适用于各近邻算法。 
(5)测试算法:编写函数使用提供的部分数据集作为测试样本，测试样本与非测试样本
的区别在于测试样本是已经完成分类的数据，如果预测分类与实际类别不同，则标记
为一个错误。 
(6)使用算法:本例没有完成此步驟，若你感兴趣可以构建完整的应用程序，从图像中提
取数字，并完成数字识别，美国的邮件分拣系统就是一个实际运行的类似系统。
'''
from numpy import *
from os import listdir

from chapter2.module_2_1 import classify0


def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    '''
    手写数字识别系统的测试代码
    :return:
    '''
    hwLabels = []
    trainingFileList = listdir('data/trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('data/trainingDigits/%s' % fileNameStr)

    testFileList = listdir('data/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('data/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with:%d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0

    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount / float(mTest))


handwritingClassTest()
