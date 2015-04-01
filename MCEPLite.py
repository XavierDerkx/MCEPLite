#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""MCEPLite.py:

Monte Carlo error propagation calculation  performed for an equation from a given
number of variables and their respective distribution.
"""

from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

__author__="Xavier Derkx"
__copyright__ = "Xavier Derkx - Tout droit reservé"
__email__ = "xavier.derkx@gmail.com"
__license__ = "CeCILL 2.1"
__version__ = "0.1"
__date__ = "2015-02-27"
__status__ = "Prototype"

# *****************************************************************************
# MAIN
# *****************************************************************************
def main():
    seed()

    Equation = raw_input("Enter the equation : ")
    NbVariables = int(input("Enter the number of variables: "))
    
    # Mean values and sigmas
    X = [[None]]*NbVariables
    MX = [[None]]*NbVariables
    EX = [[None]]*NbVariables

    # Loop on the variables for initialisation
    for i in range(0, NbVariables):
        MX[i] = float(input("Enter the mean value of the variable X[%d]: " % i))
        EX[i] = float(input("Enter the error on the variable X[%d]: " % i))
        print("Variable X[%d] = %f +/- %f " % (i, MX[i], EX[i]))

    # Number of random draws
    NbDraws = int(input("Enter the number of events to simulate: "))
    Results = [[None]]*NbDraws

    # Number of bins
    NbBins = int(input("Enter the number of bins: "))

    # Loop for the draws
    for d in range(0, NbDraws):
        for i in range(0, NbVariables):
            X[i] = gauss(MX[i],EX[i])
            #print(d,X[i])
        Results[d] = eval(Equation)
        #print(Results[d])
    
    # Definition of an histogram
    plt.figure(1)
    result = plt.hist(Results,100)
    plt.xlim((min(Results), max(Results)))

    mean = np.mean(Results)
    variance = np.var(Results)
    sigma = np.sqrt(variance)
    x = np.linspace(min(Results), max(Results),100)
    dx = result[1][1] - result[1][0]
    scale = len(Results)*dx
    plt.plot(x, mlab.normpdf(x,mean,sigma)*scale)

    plt.show()
    print("")

# *****************************************************************************
if __name__ == "__main__":
    main()

# *****************************************************************************
#Gaussian function
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
# *****************************************************************************
