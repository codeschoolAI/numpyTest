import numpy as np
import requests
import json
url = "https://491c-84-54-76-160.eu.ngrok.io/colab"
class Array1D:
    def check(self, solution):
        result = True
        if len(solution.shape) == 1 and solution.__class__ == np.ndarray:
            print("✅Accepted")
            
        else:
            result = False
            print("❌Incorrect, solution is not a 1D array")
        r = requests.post(url, json = {'result': result})
        print(r.json())
        

class ArrayZerosNxM:
    def check(self, solution):
        if solution.__class__ == np.ndarray and (solution == 0).all() == True and len(solution.shape) == 2:
            print("✅Accepted")
        else:
            print("❌Incorrect, solution is not a NxM array of zeros")

q0 = Array1D()
q1 = ArrayZerosNxM()