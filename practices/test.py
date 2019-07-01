import numpy as np

dt = np.dtype([('age', 'int8'), ('isMale', 'bool')])
a = np.array([(1,0), (2,0), (3,0)], dtype=dt)
print(a['age'])
print(a['isMale'])
print(a)
