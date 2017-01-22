import os.path
import scipy.io
import numpy as np



file_path = '/home/sameera/Documents/Mphil/DBScanClustering/MotionTubeCode/matconvnet-1.0-beta20/finalvectors/v_diving_'
saveName = 'v_diving_'


for x in range(1, 26):
    for y in range(1, 10):
	inputVector = np.zeros([15, 1000])
	if x < 10:
	    for k in range(1, 16):
            	fileName = file_path + '0' + str(x) + '_0' + str(y) + '_' + str(k)
		saveNam = saveName + '0' + str(x) + '_0' + str(y)
		if os.path.exists(fileName + '.mat'):
 			inp = scipy.io.loadmat(fileName  + '.mat')
			inputVector[k-1,:] = inp['valout']
	    if np.count_nonzero(inputVector) > 0:
	    	np.save('/home/sameera/Documents/Mphil/finalVectors/' + saveNam, inputVector)
	else:
	    for k in range(1, 16):
            	fileName = file_path + str(x) + '_0' + str(y) + '_' + str(k)
		print fileName
		saveNam = saveName + str(x) + '_0' + str(y)
		if os.path.exists(fileName + '.mat'):
			inp = scipy.io.loadmat(fileName  + '.mat')
			inputVector[k-1,:] = inp['valout']

	    if np.count_nonzero(inputVector) > 0:
	    	np.save('/home/sameera/Documents/Mphil/finalVectors/' + saveNam, inputVector)
    	 
    
