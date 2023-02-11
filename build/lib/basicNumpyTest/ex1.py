import numpy as np

class Array1D:
    def check(self, solution):
        if len(solution.shape) == 1 and solution.__class__ == np.ndarray:
            print("✅Accepted")
        else:
            print("❌Incorrect, solution is not a 1D array")

class ArrayZerosNxM:
    def check(self, solution):
        if solution.__class__ == np.ndarray and (solution == 0).all() == True and len(solution.shape) == 2:
            print("✅Accepted")
        else:
            print("❌Incorrect, solution is not a NxM array of zeros")

q0 = Array1D()
q1 = ArrayZerosNxM()