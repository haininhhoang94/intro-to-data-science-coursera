import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# Generate a lognormal random from 2832 to 2991 with mean 2883
# dataset = np.random.lognormal()

# convert X ~ N(0, 1) to Y ~ N(u, s):
# Y = X * s + u
# want Y in [a, b]:
# so X in [(a - u)/s, (b - u)/s]
#
# We want Z ~ logN(u, s) in [zmin, zmax]
# Z = exp(Y) and
# a, b = np.log((zmin, zmax))


def lognormal(a, b, loc=1, scale=1, size=1):
    a, b = np.log((a, b))
    ca, cb = (np.array((a, b)) - loc) / scale
    rv = scipy.stats.truncnorm(a=ca, b=cb)
    z = np.exp(rv.rvs(size=size) * scale + loc)
    return z


zmin, zmax = 2832, 2991
z = lognormal(zmin, zmax, 0.1, 0.1, 10000)
sns.displot(z)
plt.show()

np.savetxt("./data-lan/z.txt", z)
