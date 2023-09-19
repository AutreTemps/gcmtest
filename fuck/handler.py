import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_nf = pd.read_csv('fuck/result_No_Failure_a/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_a = pd.read_csv('fuck/result_Tsai_Wu_a/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_b = pd.read_csv('fuck/result_Tsai_Wu_b/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_c = pd.read_csv('fuck/result_Tsai_Wu_c/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_d = pd.read_csv('fuck/result_Tsai_Wu_d/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_e = pd.read_csv('fuck/result_Tsai_Wu_e/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_f = pd.read_csv('fuck/result_Tsai_Wu_f/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_g = pd.read_csv('fuck/result_Tsai_Wu_g/sensor_ndi_hit_area.csv', sep=' ', header=None)
data_h = pd.read_csv('fuck/result_Tsai_Wu_h/sensor_ndi_hit_area.csv', sep=' ', header=None)

t_a = data_a[0].to_numpy()
vx_a = data_a[1].to_numpy()
vy_a = data_a[2].to_numpy()
vz_a = data_a[3].to_numpy()
v_a = np.sqrt(vx_a**2 + vy_a**2 + vz_a**2)

t_b = data_b[0].to_numpy()
vx_b = data_b[1].to_numpy()
vy_b = data_b[2].to_numpy()
vz_b = data_b[3].to_numpy()
v_b = np.sqrt(vx_b**2 + vy_b**2 + vz_b**2)

t_c = data_c[0].to_numpy()
vx_c = data_c[1].to_numpy()
vy_c = data_c[2].to_numpy()
vz_c = data_c[3].to_numpy()
v_c = np.sqrt(vx_c**2 + vy_c**2 + vz_c**2)

t_d = data_d[0].to_numpy()
vx_d = data_d[1].to_numpy()
vy_d = data_d[2].to_numpy()
vz_d = data_d[3].to_numpy()
v_d = np.sqrt(vx_d**2 + vy_d**2 + vz_d**2)

t_e = data_e[0].to_numpy()
vx_e = data_e[1].to_numpy()
vy_e = data_e[2].to_numpy()
vz_e = data_e[3].to_numpy()
v_e = np.sqrt(vx_e**2 + vy_e**2 + vz_e**2)

t_f = data_f[0].to_numpy()
vx_f = data_f[1].to_numpy()
vy_f = data_f[2].to_numpy()
vz_f = data_f[3].to_numpy()
v_f = np.sqrt(vx_f**2 + vy_f**2 + vz_f**2)

t_g = data_g[0].to_numpy()
vx_g = data_g[1].to_numpy()
vy_g = data_g[2].to_numpy()
vz_g = data_g[3].to_numpy()
v_g = np.sqrt(vx_g**2 + vy_g**2 + vz_g**2)

t_h = data_h[0].to_numpy()
vx_h = data_h[1].to_numpy()
vy_h = data_h[2].to_numpy()
vz_h = data_h[3].to_numpy()
v_h = np.sqrt(vx_h**2 + vy_h**2 + vz_h**2)

t_nf = data_nf[0].to_numpy()
vx_nf = data_nf[1].to_numpy()
vy_nf = data_nf[2].to_numpy()
vz_nf = data_nf[3].to_numpy()
v_nf = np.sqrt(vx_nf**2 + vy_nf**2 + vz_nf**2)

fig, ax = plt.subplots()

ax.set_xlabel('time, seconds')
ax.set_ylabel('$V_z$, m/s')
ax.set_title('Tsai Wu vs No failure model (impact point area)')

ax.set_xlim(0.000015, 0.00007)

t = t_e

v_max = np.array([max(v_a[i], v_b[i], v_c[i], v_d[i], v_e[i], v_f[i], v_g[i], v_h[i]) for i in range(len(t))])
v_min = np.array([min(v_a[i], v_b[i], v_c[i], v_d[i], v_e[i], v_f[i], v_g[i], v_h[i]) for i in range(len(t))])

#ax.plot(t_a, v_a, zorder=5, label='Tsai Wu (A)')
#ax.plot(t_b, v_b, zorder=5, label='Tsai Wu (B)')
#ax.plot(t_c, v_c, zorder=5, label='Tsai Wu (C)')
#ax.plot(t_d, v_d, zorder=5, label='Tsai Wu (D)')
#ax.plot(t_e, v_e, zorder=5, label='Tsai Wu (E)')
#ax.plot(t_f, v_f, zorder=5, label='Tsai Wu (F)')
#ax.plot(t_g, v_g, zorder=5, label='Tsai Wu (G)')
#ax.plot(t_h, v_h, zorder=5, label='Tsai Wu (H)')
#ax.plot(t, v_max, color='b', zorder=5, label='Max')
#ax.plot(t, v_min, color='b', zorder=5, label='Min')
ax.fill_between(t, v_min, v_max, color='black', alpha=0.4, zorder=4, label='Tsai Wu criterion')
ax.plot(t_nf, v_nf, color='black', linestyle='--', zorder=5, label='No failure')

ax.legend()
ax.grid(zorder=2)

#plt.show()
plt.savefig('Top_area.png')