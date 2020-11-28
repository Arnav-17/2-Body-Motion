import numpy as np
G = 6.67*10**-11    # Gravitational Constant
M = 1.99*10**30     # Mass of Sun
m = 10**14     # Mass of Planet
C = G*M*m
t_r = 200*365       # period of revolution of planet in days
h = 0.001
AU = 1.496*10**11
Api = 1*AU     # Aphelion distance
Peri = 8.3*AU         # Perihelion distance
A = Peri
E = C/A            # Energy of system
e = 2.7     # Eccentricity of orbit
L = np.sqrt(m*C**2*(e**2 - 1)/(2*E))
r_0 = L**2/(G*M*m**2)   # Dimensionless position
t_0 = L**3/(G**2*M**2*m**3)     # Dimensionless time
r = Peri/r_0        # Initial value of position
t = t_r*24*60*60/(t_0*h)   # Number of time steps to be taken
print(r)
print(r_0)
print(t)
