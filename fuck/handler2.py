import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_nf = pd.read_csv('fuck/result_No_Failure_a/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_a = pd.read_csv('fuck/result_Tsai_Wu_a/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_b = pd.read_csv('fuck/result_Tsai_Wu_b/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_c = pd.read_csv('fuck/result_Tsai_Wu_c/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_d = pd.read_csv('fuck/result_Tsai_Wu_d/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_e = pd.read_csv('fuck/result_Tsai_Wu_e/sensor_ndi_collision_line.csv', sep=' ', header=None)

t_a = data_a[0].to_numpy()
vz_a = data_a[3].to_numpy()

t_b = data_b[0].to_numpy()
vz_b = data_b[3].to_numpy()

t_c = data_c[0].to_numpy()
vz_c = data_c[3].to_numpy()

t_d = data_d[0].to_numpy()
vz_d = data_d[3].to_numpy()

t_e = data_e[0].to_numpy()
vz_e = data_e[3].to_numpy()

t_nf = data_nf[0].to_numpy()
vz_nf = data_nf[3].to_numpy()

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.set_xlabel('time')
ax.set_ylabel('$V_z$')
ax.set_title('Tsai Wu vs No failure model (collision line)')

ax.set_xlim(0, 0.00007)

ax.plot(t_a, vz_a, zorder=5, label='Tsai Wu (A)')
ax.plot(t_b, vz_b, zorder=5, label='Tsai Wu (B)')
ax.plot(t_c, vz_c, zorder=5, label='Tsai Wu (C)')
ax.plot(t_d, vz_d, zorder=5, label='Tsai Wu (D)')
ax.plot(t_e, vz_e, zorder=5, label='Tsai Wu (E)')
ax.plot(t_nf, vz_nf, zorder=5, label='No failure')

ax.legend()

#plt.show()
plt.savefig('abcde.png')