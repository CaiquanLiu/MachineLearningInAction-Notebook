# coding:utf-8
'''
Created on 2017/11/21 下午4:14

@author: liucaiquan
'''
'''
(1)收集数据:提供的文本文件。
(2)准备数据:解析tab键分隔的数据行。
(3)分析数据:快速检查数据，确保正确地解析数据内容，使用creatPlot()函数绘制 最终的树形图。
(4)训练算法:使用3.1节的createTree()函数。 
(5)测试算法:编写测试函数验证决策树可以正确分类给定的数据实例。 
(6)使用算法:存储树的数据结构，以便下次使用时无需重新构造树。
'''
from module_3_1 import createTree
from module_3_2 import createPlot

fr = open('data/lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
print lenses
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
# 测试结果与预期不符合
lensesTree = createTree(lenses, lensesLabels)
print lensesTree

createPlot(lensesTree)
