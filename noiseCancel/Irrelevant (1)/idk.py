import numpy as np
import matplotlib.pylab as plt

import padasip as pa

#%matplotlib inline 
plt.style.use('ggplot') # nicer plots
np.random.seed(52102) # always use the same random seed to make results comparable
#%config InlineBackend.print_figure_kwargs = {}


# signals creation: u, v, d
N = 5000
n = 10
u = np.sin(np.arange(0, N/10., N/50000.))
v = np.random.normal(0, 1, N)
d = u + v

# filtering
x = pa.input_from_history(d, n)[:-1]
d = d[n:]
u = u[n:]
f = pa.filters.FilterRLS(mu=0.9, n=n)
y, e, w = f.run(d, x)

# error estimation
MSE_d = np.dot(u-d, u-d) / float(len(u))
MSE_y = np.dot(u-y, u-y) / float(len(u))

# results
plt.figure(figsize=(12.5,6))
plt.plot(u, "r:", linewidth=4, label="original")
plt.plot(d, "b", label="noisy, MSE: {}".format(MSE_d))
plt.plot(y, "g", label="filtered, MSE: {}".format(MSE_y))
plt.xlim(N-100,N)
plt.legend()
plt.tight_layout()
plt.show()
