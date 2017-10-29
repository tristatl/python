#coding: utf-8
'''
Created on 2017年10月29日

@author: TangLi
'''
from numpy import *
import operator
import matplotlib.pyplot as plt
import matplotlib
from test.test_audioop import datas

#生成样本集，及其分类结果
def CreateDataSet():
    group = array([[1,2],[3,4]])
    labels = array(['A','A','B','B'])
    return group, labels


#kNN算法，inX待测样本，dataSet样本集，labels样本集分类结果，k近邻数目
def classifyKNN(inX, dataSet, labels, k):
    
    #array.shape(),各维度的大小，shape[0]第一维的长度
    dataSetSize = dataSet.shape[0]
    #print 'dataSetSize', dataSetSize
    
    #计算待测点到样本集各点的距离,欧式距离公式
    #array.tile(array,(...,c,b,a))，
    #复制按照，从右到左，从最大的维度开始复制(即从最里面的括号[[[],[]]])开始复制，1就是原来的大小，2复制一倍
    #numpy中的算术操作符是elementwize，按元素操作
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    #print 'tile(inX, (dataSetSize,1))', tile(inX, (dataSetSize,1))
    #print 'diffMat', diffMat
    
    #平方
    sqDiffMat = diffMat**2
    #print 'sqDiffMat', sqDiffMat
    
    #平方和
    #按照第二维度的数和相加
    sqDistance = sqDiffMat.sum(axis = 1)
    #print 'sqDistance', sqDistance
    
    #开方
    distances = sqDistance**0.5
    #print 'distances', distances
    
    #排序，返回值从小到大排序的数的下标
    sortedDistIndicies = distances.argsort()
    #print 'sortedDistIndicies', sortedDistIndicies
    
    #字典{key:value}
    classCount = {}
    
    #计算离待测样本最近的前k个点的标签最多的是哪个
    for i in range(k):
        
        #下标为i的样本的标签
        voteIlabel = labels[sortedDistIndicies[i]]
        
        #该标签计数+1
        #get()查看字典中是否有该关键字，如果没有就使值为0
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        
    #标签排序，key = operator.itemgetter(1)按字典中1号下标排序(即value)，降序
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    
    #返回标签最多的key
    return sortedClassCount[0][0]


#将文本记录转为NumPy的解析程序
def file2matrix(filename):
    
    #打开文件
    fr = open(filename)
    #按行读取
    arrayOfLines = fr.readlines()
    #行数
    numberOfLines = len(arrayOfLines)
    #array.zeros()用0填充数组
    retMat = zeros((numberOfLines, 3))
    #不定长数组
    classLabelVetor = []
    index = 0
    #循环读取文件
    for line in arrayOfLines:
        #strip(char)截取行首尾字符，strip()默认截取空格
        line = line.strip()
        #split()按'\t'分割
        listFromLine = line.split('\t')
        #返回数组[第index行,:]全部数，[0:3]下标0到3
        retMat[index, :] = listFromLine[0:3]
        #[-1]倒数第一列
        classLabelVetor.append(int(listFromLine[-1]))
        index += 1
    #返回样本集及标签集
    return retMat,classLabelVetor


#测试file2matrix(filename)函数
datingDataMat, datingLabels = file2matrix(r'dataTestSet.txt')
#print datingDataMat[0:20],'\n', datingLabels[0:20]


'''
#画布
fig = plt.figure()

#一行一列的一个图表
ax = fig.add_subplot(111)

#散点图（x,y）, datingDataMat[[i]]第一个数为x, datingDataMat[[i]]第二个数为y，datingDataMat[:]所有行
#第一个15*array(datingLabels)表示点的大小，第二个15*array(datingLabels)表示点的颜色
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15*array(datingLabels), 15*array(datingLabels))
plt.show()
'''

#数据归一化，避免其中某项数据因为单位太大，而造成对结果影响太大
#归一化公式 newValue = (oldValue-min)/(max-min)
def autoNorm(dataSet):
    #0第一维，[[],[]],最外面的括号,返回各列的最小值
    minVals = dataSet.min(0)
    #各列的最大值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    #样本大小
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals    


'''
#测试autoNorm(dataSet)函数
normMat, ranges, minVals = autoNorm(datingDataMat)    
print normMat
print ranges
print minVals
'''


#分类器针对约会网站的测试算法
def datingClassTest(): 
    hoRatio = 0.10
    #样本集，标签集
    datingDataMat, datingLabels = file2matrix('dataTestSet.txt')
    #归一化后
    normMat, ranges, minVals = autoNorm(datingDataMat)
    #样本大小
    m = normMat.shape[0]
    #10%作为测试样本集
    numTestVecs = int(m*hoRatio)
    #错误个数
    errorCnt = 0.0
    #测试样本集中预测分类错误的个数
    for i in range(numTestVecs):
        #预测第i个测试样本的分类
        #normMat[numTestVecs:m,:],numTestVecs到m行的每行的所有下标数据
        classifierRes = classifyKNN(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with : %d, the real answer is: %d" % (classifierRes, datingLabels[i])
        #若和它真实的类型不同，错误个数++
        if(classifierRes != datingLabels[i]):
            errorCnt += 1
            #计算出错率
            print "the total error rate is: %f" % (errorCnt/float(numTestVecs))
    
#测试datingClassTest()函数
datingClassTest()   



    
    
    
    