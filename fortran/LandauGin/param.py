import numpy as np
#arguments go like g, beta, N, endT

kappaL = [i for i in np.linspace(1,1,1)]
betaL = [i for i in np.linspace(10,10,1)]
mu = 0

params = np.array([(k,beta,mu, 300,10001) for k in kappaL for beta in betaL])

np.savetxt('params.txt',params,delimiter=' ',fmt=['%03.2f','%04.3f','%04.3f','%d','%d'])


