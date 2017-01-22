import os.path
import scipy.io
import numpy as np



file_path = '/home/sameera/Documents/Mphil/55/StandUp'
saveName = 'StandUp'


for x in range(1, 1000):
	inputVector = np.zeros([15, 1000])
	if x < 10:
	    for k in range(1, 10):
            	fileName = file_path + '0000' + str(x) + '_' + str(k)
		saveNam = saveName + '0000' + str(x)
		if os.path.exists(fileName + '.mat'):
 			inp = scipy.io.loadmat(fileName  + '.mat')
			inputVector[k-1,:] = inp['valout']
	    if np.count_nonzero(inputVector) > 0:
	    	np.save('/home/sameera/Documents/Mphil/hollywoodCombined/' + saveNam, inputVector)
	elif 10<=x and x<100:
	    for k in range(1, 10):
            	fileName = file_path + '000' + str(x) + '_' + str(k)
		saveNam = saveName + '000' + str(x)

		if os.path.exists(fileName + '.mat'):
 			inp = scipy.io.loadmat(fileName  + '.mat')
			inputVector[k-1,:] = inp['valout']

	    if np.count_nonzero(inputVector) > 0:
	    	np.save('/home/sameera/Documents/Mphil/hollywoodCombined/' + saveNam, inputVector)

	else:
	    for k in range(1, 10):
            	fileName = file_path + '00' + str(x) + '_' + str(k)
		saveNam = saveName + '00' + str(x)
		if os.path.exists(fileName + '.mat'):
 			inp = scipy.io.loadmat(fileName  + '.mat')
			inputVector[k-1,:] = inp['valout']
	    if np.count_nonzero(inputVector) > 0:
	    	np.save('/home/sameera/Documents/Mphil/hollywoodCombined/' + saveNam, inputVector)
    	 
    
