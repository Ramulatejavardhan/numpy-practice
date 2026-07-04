import numpy as np
score=np.array([91,99,100,12])
# print(score==100)
score[score<90]=0
print(score)