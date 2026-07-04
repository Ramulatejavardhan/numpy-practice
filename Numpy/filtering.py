import numpy as np
ages=np.array([12,23,34,56,67,78,10,89,99,22,21,20])
adult=ages[ages>18]
print(adult)
where=np.where(ages<18,ages,0)