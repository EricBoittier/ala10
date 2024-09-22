import numpy as np

# boltzmann constant in units of (kcal/mol)/K
boltzmann = 1.987204259*10**-3
FONTSIZE = 20


# helper functions
def running_mean(x, N=1000):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)
   
def jarzynski(forces, velocity=1.0, dt=0.1, T=300.0):
    beta = 1/(boltzmann*T)
    work = velocity*dt*np.cumsum(forces)
    dG = -(1/beta)*np.log(np.exp(work*-beta))
    return dG