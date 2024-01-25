#%%
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

#%%
# Voorbeeld van die spline interpolasie:
theta = 2 * np.pi * np.linspace(0, 1, 5)

y = np.c_[np.cos(theta), np.sin(theta)]

cs = CubicSpline(theta, y, bc_type='periodic')

print("ds/dx={:.1f} ds/dy={:.1f}".format(cs(0, 1)[0], cs(0, 1)[1]))
#ds/dx=0.0 ds/dy=1.0

xs = 2 * np.pi * np.linspace(0, 1, 100)

fig, ax = plt.subplots(figsize=(6.5, 4))

ax.plot(y[:, 0], y[:, 1], 'o', label='data')

ax.plot(np.cos(xs), np.sin(xs), label='true')

ax.plot(cs(xs)[:, 0], cs(xs)[:, 1], label='spline')

ax.axes.set_aspect('equal')

ax.legend(loc='center')

plt.show()
# %%

airfoil = np.loadtxt('HQ34.dat', skiprows=1)

# %%
plt.plot(airfoil[:,0], airfoil[:,1])
plt.title('Plot the airfoil')
# %%
cs = CubicSpline(airfoil[0:20,0], airfoil[0:20,1], bc_type='periodic')



# %%
#https://stackoverflow.com/questions/67460967/cubic-spline-for-non-monotonic-data-not-a-1d-function

import numpy
import scipy.interpolate
import matplotlib.pyplot as plt

#path_x = numpy.asarray((4.0, 5.638304088577984, 6.785456961280076, 5.638304088577984, 4.0),dtype=float)
#path_y = numpy.asarray((0.0, 1.147152872702092, 2.7854569612800755, 4.423761049858059, 3.2766081771559668),dtype=float)
path_x=airfoil[i,0]
path_y=airfoil[i,1]

# defining arbitrary parameter to parameterize the curve
path_t = numpy.linspace(0,1,path_x.size)

# this is the position vector with
# x coord (1st row) given by path_x, and
# y coord (2nd row) given by path_y
r = numpy.vstack((path_x.reshape((1,path_x.size)),path_y.reshape((1,path_y.size))))

# creating the spline object
spline = scipy.interpolate.interp1d(path_t,r,kind='cubic')

# defining values of the arbitrary parameter over which
# you want to interpolate x and y
# it MUST be within 0 and 1, since you defined
# the spline between path_t=0 and path_t=1
t = numpy.linspace(numpy.min(path_t),numpy.max(path_t),100)

# interpolating along t
# r[0,:] -> interpolated x coordinates
# r[1,:] -> interpolated y coordinates
r = spline(t)

plt.plot(path_x,path_y,'or')
plt.plot(r[0,:],r[1,:],'-k')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# %%

#https://numpy.org/doc/stable/user/quickstart.html#indexing-with-arrays-of-indices
i = np.array([0, 3, 10, 20, 30, 50, 60, 70, 75, 80, 90, 100, 105, 110, 115, 120, 130, 140, 147, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 262])
print(airfoil[i,0])

# Select the airfoil points as above.
# make a spline with the subset
# But make the spline a path dependant function
# %%

# or try b-splines

from scipy.interpolate import BSpline

k = 2

t = [0, 1, 2, 3, 4, 5, 6]

c = [-1, 2, 0, -1]

spl = BSpline(t, c, k)

spl(2.5)


# %%
airfoilspline = BSpline(path_x, path_y, 2)
# %%
