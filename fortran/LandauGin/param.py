import numpy as np
#arguments go like g, beta, N, endT

kappaL = [i for i in np.linspace(1,1,1)]
betaL = [i for i in np.linspace(10,10,1)]
seed = [i for i in np.arange(10)]
mu = 0
gridSize = 200
endTime = 501

params = np.array([(k,beta,mu, gridSize,endTime,s) for k in kappaL for beta in betaL for s in seed])

np.savetxt('params.txt',params,delimiter=' ',fmt=['%03.2f','%04.3f','%04.3f','%d','%d','%d'])


