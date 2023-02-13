
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
import scipy as sp
from scipy.integrate import odeint

# Setup the time
Time_Start          = 0                                                 # Starting time (s)
Time_End            = 2                                                 # End time (s)
TIMESTEP            = 0.001                                             # Timeinterval (s)
Start_Angle         = 0
End_Angle           = 90
n_Calculations      = int(Time_End/TIMESTEP)                            # Number of calculations
Time                = np.linspace(Time_Start,Time_End, n_Calculations)  # Building a time table (s)
Angle               = np.linspace(Start_Angle,End_Angle,n_Calculations)                  # Vuilding a table in which the angle of the cone changes (degree)

x_data              = Time                                      # Name clearification
y_data              = Angle                                     # Name clearification
X, Y                = np.meshgrid(x_data, y_data)               # Building two dimentional tables, needed for caluclating surface plot

# Setting up constantes and varables
Mass                = 0.00125                                   # Mass of cone (kg)
g                   = -9.81                                     # Gravitational acceleration (m/s^2)
Hypotenuse          = 0.073                                     # Length of teh side of the cone (m)
Dencity             = 1.2                                       # Air dencity at sealevel (kg/m^3)
Cd                  = 0.0112*y_data+0.162                       # Air resistance coeficient (no unit)
Radius              = Hypotenuse * np.sin(Angle*math.pi/180)    # Small radius of cone (m)
A                   = math.pi * Radius**2                       # Area of base of the cone (m^2)
K                   = 0.5 * Dencity * Cd * A / Mass             # Calculating constante K to simplefy the differential equation
v0                  = np.zeros(n_Calculations)                  # Starting velocity (m/s)
h0                  = v0                                        # Starting hight (m)

# Differential solver
def dvdt(v, t):
    return (g + K * v ** 2) 

# Calling differential solver 
V = odeint(dvdt, y0=v0, t=Time)
X = np.rot90(np.rot90(np.rot90(X)))
Y = np.rot90(Y)

#Plotting
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, V)
ax.set_xlabel('Time')
ax.set_ylabel('Angle')
ax.set_zlabel('Hight')
plt.show()
