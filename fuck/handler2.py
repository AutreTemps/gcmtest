import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_nf = pd.read_csv('fuck/result_No_Failure_a/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_a = pd.read_csv('fuck/result_Tsai_Wu_a/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_b = pd.read_csv('fuck/result_Tsai_Wu_b/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_c = pd.read_csv('fuck/result_Tsai_Wu_c/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_d = pd.read_csv('fuck/result_Tsai_Wu_d/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_e = pd.read_csv('fuck/result_Tsai_Wu_e/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_f = pd.read_csv('fuck/result_Tsai_Wu_f/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_g = pd.read_csv('fuck/result_Tsai_Wu_g/sensor_ndi_collision_line.csv', sep=' ', header=None)
data_h = pd.read_csv('fuck/result_Tsai_Wu_h/sensor_ndi_collision_line.csv', sep=' ', header=None)

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

t_f = data_f[0].to_numpy()
vz_f = data_f[3].to_numpy()

t_g = data_g[0].to_numpy()
vz_g = data_g[3].to_numpy()

t_h = data_h[0].to_numpy()
vz_h = data_h[3].to_numpy()

t_nf = data_nf[0].to_numpy()
vz_nf = data_nf[3].to_numpy()

fig, ax = plt.subplots()

ax.set_xlabel('time, seconds')
ax.set_ylabel('$V_z$, m/s')
ax.set_title('Tsai Wu vs No failure model (impact line)')

ax.set_xlim(0.000015, 0.00007)

t = t_e

v_max = np.array([max(vz_a[i], vz_b[i], vz_c[i], vz_d[i], vz_e[i], vz_f[i], vz_g[i], vz_h[i]) for i in range(len(t))])
v_min = np.array([min(vz_a[i], vz_b[i], vz_c[i], vz_d[i], vz_e[i], vz_f[i], vz_g[i], vz_h[i]) for i in range(len(t))])

#ax.plot(t_a, vz_a, zorder=5, label='Tsai Wu (A)')
#ax.plot(t_b, vz_b, zorder=5, label='Tsai Wu (B)')
#ax.plot(t_c, vz_c, zorder=5, label='Tsai Wu (C)')
#ax.plot(t_d, vz_d, zorder=5, label='Tsai Wu (D)')
#ax.plot(t_e, vz_e, zorder=5, label='Tsai Wu (E)')
#ax.plot(t_f, vz_f, zorder=5, label='Tsai Wu (F)')
#ax.plot(t_g, vz_g, zorder=5, label='Tsai Wu (G)')
#ax.plot(t_h, vz_h, zorder=5, label='Tsai Wu (H)')
#ax.plot(t, v_max, color='b', zorder=5, label='Max')
#ax.plot(t, v_min, color='b', zorder=5, label='Min')
ax.fill_between(t, v_min, v_max, color='black', alpha=0.4, zorder=4, label='Tsai Wu criterion')
ax.plot(t_nf, vz_nf, color='black', linestyle='--', zorder=5, label='No failure')

ax.legend()
ax.grid(zorder=2)

#plt.show()
plt.savefig('Impact_line.png')