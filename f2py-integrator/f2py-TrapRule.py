import time
import numpy as np
import math as m
import matplotlib.pyplot as plt
import TrapIntg_elRod as TIeR


# CONSTANTS
PI      = np.pi     # radians [dimless]
L       = 1.0       # meters
lambda0 = 0.3       # Coloumb/meters
eps0    = 8.854e-11 # Farads/meters

# THE EXACT SOLUTION
# OBS: Takes x/L as argument, instead of only x

Phi_Res = 1000 # Resolution in phi: no. of times to perform the integral
Int_Res = 1000 # Resolution in the integral: Trapezoidal method

L = 1.0

x_list   = np.linspace(0, L, Phi_Res)
phi_x_ex = np.zeros(Phi_Res)

    
def ExactSolution(xL):
    Term1 = m.sqrt((xL - L)**2 + 1) - xL*m.asinh(xL - L) # z = L
    Term2 = m.sqrt((xL - 0)**2 + 1) - xL*m.asinh(xL - 0) # z = 0
    return Term1 - Term2
    
for i in range(Phi_Res):
    phi_x_ex[i] = ExactSolution(x_list[i]/L)


# Check the documentation of out Fortran Module:
print("--------------------------------")
print(TIeR.__doc__)
print("--------------------------------")


start  = time.time()
phi_x  = TIeR.trapezoidalintegrator(np.array(Phi_Res), np.array(Int_Res), L)
end    = time.time()

F2PYtime = end-start
print("Elapsed time (s): ", round(F2PYtime,4))

plt.figure(figsize=(10,6))
plt.title('Exact vs (F2PY) Numerical Solution')
plt.ylabel('C Psi(z)')
plt.xlabel('z=x/L')
plt.plot(x_list,phi_x_ex,color='g', linestyle='-', linewidth=3.0, label='Exact')
plt.plot(x_list,phi_x,   color='r', linestyle='--',linewidth=3.0, label='Numerical')
plt.legend(loc=4)
plt.show()
