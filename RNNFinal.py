from __future__ import division, print_function, absolute_import
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.datasets import imdb


import glob, os
import os.path
import scipy.io
import numpy as np

import tflearn


file_path = '/home/sameera/Documents/Mphil/hollywoodCombined/'
os.chdir(file_path)
count = 0;
totalMatX = np.zeros([1, 15, 1000])
totalListY = [];
for file in glob.glob("*.npy"):
	if "StandUp" in str(file):
		totalListY.append(1);
	else:
		totalListY.append(0); 
	count = count +1
	if count == 1:
		totalMatX[0,:,:] = np.load(file_path  + file)
	else:
		tempMat = np.zeros([1, 15, 1000])
		tempMat[0,:,:] = np.load(file_path  + file)
		totalMatX = np.append(totalMatX,tempMat,axis=0)

print (totalMatX.shape)
print (len(totalListY))

totalListY = to_categorical(totalListY, nb_classes=2)

numSamples = totalMatX.shape[0];
numTrainSamples = int(numSamples*70/100)

x = np.random.rand(numSamples, 15, 1000)
indices = np.random.permutation(x.shape[0])
training_idx, test_idx = indices[:numTrainSamples], indices[numTrainSamples:]
trainingX, testX = totalMatX[training_idx,:], totalMatX[test_idx,:]
trainingY, testY = totalListY[training_idx,:], totalListY[test_idx,:]


print (trainingX.shape)
print (testX.shape)
print (trainingY.shape)
print (testY.shape)

print ("##########training network")
net = tflearn.input_data([None, 15, 1000])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                         loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(trainingX, trainingY, validation_set=(testX, testY), show_metric=True,
          batch_size=5)		    
