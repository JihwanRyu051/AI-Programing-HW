import math
import random

class Setup:
    def __init__(self, parameters):
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
        self._aType = parameters['aType']

    def getAType(self):
        return self._aType


