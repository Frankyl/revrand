"""
Likelihood objects for inference within the GLM framework.
"""

import numpy as np
from .utils import Positive


class Gaussian():

    def __init__(self, var_bounds=Positive()):

        self.bounds = [var_bounds]

    def loglike(self, y, f, var):

        N = len(f)

        return -0.5 * (N * np.log(2 * np.pi * var) + ((y - f)**2).sum() / var)

    def Ey(self, f, var):

        return f

    def df(self, y, f, var):

        return (y - f) / var

    def d2f(self, y, f, var):

        return - 1. / var * np.ones_like(f)
