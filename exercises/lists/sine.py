import math
import numpy as np
import matplotlib.pyplot as plt

# create a list of angles
angles_deg = np.arange(0 , 90, 0.1)
alpha_rad = angles_deg * np.pi / 180
x = angles_deg
y = np.sin(alpha_rad)

# print(x)

# y = []
# for angle_deg in angles_deg:
#     # π rad = 180°, 1° = π/180°
#     # α(radians) = α(degrees) × π / 180°
#     alpha_deg = angle_deg * np.pi / 180
#     y.append(np.sin(alpha_deg))
# # print(y)

plt.plot(x,y)
plt.show()

