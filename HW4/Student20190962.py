import sys
import numpy as np
import operator
import os
from numpy import *
import math

argv1 = sys.argv[1]
argv1_list = os.listdir(argv1)
argv2 = sys.argv[2]
argv2_list = os.listdir(argv2)

def createDataSet(file):
	data = zeros((1, 1024))
	f = open(file)
	for i in range(32):
		line = f.readline()
		for j in range(32):
			data[0, 32*i+j] = int(line[j])
	return data

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def check():
	label = [] 
	Mat = zeros((len(argv1_list), 1024))
	for i in range(len(argv1_list)):
		name = argv1_list[i]
		name1 = name.split('.')[0]
		num = int(name1.split('_')[0])
		label.append(num)
		Mat[i, :] = createDataSet(argv1 + '/' + name)
	for n in range(20): 
		err = 0
		for j in range(len(argv2_list)):
			name2 = argv2_list[j]
			name3 = name2.split('.')[0]
			num1 = int(name3.split('_')[0])
			inX = createDataSet(argv2 + '/' + name2)
			result = classify0(inX, Mat, label, n+1)
			if int(result) != num1:
				err += 1
		print(math.floor(err/len(argv2_list)*100))
check()	
		
