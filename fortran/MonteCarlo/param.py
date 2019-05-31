import numpy as np
#arguments go like g, beta, N, endT

gL = [i for i in np.linspace(1,1,1)]
betaL = [i for i in np.linspace(20,20,1)]
mu = 0

params = np.array([(g,beta,mu, 200,100000) for g in gL for beta in betaL])

np.savetxt('params.txt',params,delimiter=' ',fmt=['%03.2f','%04.3f','%04.3f','%d','%d'])


