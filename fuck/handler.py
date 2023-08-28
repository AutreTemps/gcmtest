import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('fuck/result_csv_test/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_tw = pd.read_csv('fuck/result_Tsai_Wu/sensor_ndi_collision_line.csv', sep=' ', header=None)

t = data[0].to_numpy()
vz = data[3].to_numpy()

t_tw = data_tw[0].to_numpy()
vz_tw = data_tw[3].to_numpy()

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.set_xlabel('time')
ax.set_ylabel('$V_{z}$')
ax.set_title('Tsai Wu vs no failure model')

ax.plot(t, vz, zorder=5, label='No failure model')
ax.plot(t_tw, vz_tw, color='r', zorder=4, label='Tsai Wu failure model')

ax.legend()

plt.savefig('vz_comparison.png')