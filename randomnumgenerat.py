import numpy as np
rand=np.random.default_rng()
# print(rand.integers(1,100,size=4))
# np.random.seed(seed=1)
# print(np.random.uniform())

#random number or a alphabet from given data
emoji=(["😀","😂","😉","😆","🤗","😚","😗","🙁","😟","😦"])
emoj=rand.choice(emoji,size=2)
print(emoj)