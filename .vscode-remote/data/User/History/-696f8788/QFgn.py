import numpy as np

def calculate(list):
if len(list)!= 9:
    rise ValueError ("List must contain nine numbers.")
m=np.array(list).reshape(3,3)
calculate={
 'mean': [m.mean(axis=0).tolist, m.mean(axis=1).tolist, m.mean().tolist],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}


    return calculations