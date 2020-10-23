# Imports
import math
import sys

class CalculateCircleArea:

    def calculateCircle(self):
        v1 = float(1.1)
        r1 = v1 ** 2 * math.pi
        print(r1)
        return r1
        sys.exit()

from main import CalculateCircleArea
main = CalculateCircleArea()
main.calculateCircle()