import pandas as pd
import numpy as np

dataset = pd.read_csv('dataset\ruspini.csv')
datatraining = np.array(dataset)[:,1:-1]
print (" Data training are: ",datatraining)