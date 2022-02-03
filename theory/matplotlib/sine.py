import math
import numpy as np
import matplotlib.pyplot as plt

# create a list of angles
# angles_deg = np.arange(0, 360, 0.1)
angles_deg = list(range(0, 360, 1))
print(angles_deg)

angles_rad = []
for angle_deg in angles_deg:
    angles_rad.append(angle_deg * math.pi / 180)
print(angles_rad)

y = []
for angle in angles_rad:
    y.append(math.sin(angle))
print(y)

plt.xlim([0, 360])

plt.plot(angles_deg, y)
# # plt.plot(angles_rad, y)

plt.show()

