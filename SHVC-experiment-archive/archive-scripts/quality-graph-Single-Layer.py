import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.ticker as ticker

tick_spacing = 1.0

#SVC
psnr_svc_paris_y = [25.757, 29.710, 32.414, 35.334, 37.698, 41.596]
psnr_svc_paris_u = [32.915, 35.456, 37.496, 39.563, 41.391, 44.255]
psnr_svc_paris_v = [33.601, 35.863, 37.775, 39.683, 41.528, 44.497]
bitrate_svc_paris = [107.41, 248.87, 424.25, 734.12, 1146.04, 2252.77]
psnr_svc_paris = [0]*6
for i in range(0,6):
    psnr_svc_paris[i] = (4*psnr_svc_paris_y[i] + psnr_svc_paris_u[i] + psnr_svc_paris_v[i])/6.0
    
psnr_svc_foreman_y = [28.309, 31.844, 34.137, 36.552, 38.391, 41.432]
psnr_svc_foreman_u = [37.796, 39.165, 40.517, 41.565, 42.660, 44.722]
psnr_svc_foreman_v = [38.929, 41.100, 42.573, 44.250, 45.612, 47.349]
bitrate_svc_foreman = [82.55, 172.60, 282.99, 484.16, 748.74, 1641.03]
psnr_svc_foreman = [0]*6
for i in range(0,6):
    psnr_svc_foreman[i] = (4*psnr_svc_foreman_y[i] + psnr_svc_foreman_u[i] + psnr_svc_foreman_v[i])/6.0
    


#SHVC
psnr_shvc_paris = [23.2948, 26.0727, 28.9736, 31.9957, 35.1915, 38.6060]
bitrate_shvc_paris = [14.6960, 31.9360, 62.3800, 114.7740, 211.2220, 409.6740]

psnr_shvc_foreman = [ 26.6767, 29.2754, 31.7931, 34.2970, 36.9466, 39.7245]
bitrate_shvc_foreman = [ 9.8820, 18.1940, 33.8700, 63.1520, 120.6240, 245.4500]

#VVC
psnr_vvc_paris = [ 29.2739, 32.7191, 35.2215, 37.7194, 39.8825, 43.0179]
bitrate_vvc_paris = [64.3392, 128.9256, 207.5832, 334.6488, 503.2512, 900.4176 ]

psnr_vvc_foreman = [31.9461, 34.8504, 36.9323, 38.9610, 40.6649, 43.2429]
bitrate_vvc_foreman = [30.0264, 60.6000, 101.5968, 171.8592, 269.2032, 559.7376]

#-------------------------------PLOTS--------------------------------------

fig, plots = plt.subplots(2, 1)
#fig, bx = plt.subplots()
plots[0].plot(bitrate_svc_paris,  psnr_svc_paris,  'r', label='SVC')#, marker='s')
plots[0].plot(bitrate_shvc_paris, psnr_shvc_paris, 'b', label='SHVC')#, marker='s')
plots[0].plot(bitrate_vvc_paris,  psnr_vvc_paris,  'g', label='VVC')#, marker='s')
plots[0].grid()
plots[0].set_title('paris')
#plt.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plots[1].plot(bitrate_svc_foreman,  psnr_svc_foreman,  'r', label='SVC')#, marker='s')
plots[1].plot(bitrate_shvc_foreman, psnr_shvc_foreman, 'b', label='SHVC')#, marker='s')
plots[1].plot(bitrate_vvc_foreman,  psnr_vvc_foreman,  'g', label='VVC')#, marker='s')
plots[1].grid()
plots[1].set_title('foreman')


plots[0].set(xlabel='bitrate', ylabel='PSNR')
plots[1].set(xlabel='bitrate', ylabel='PSNR')
fig.suptitle('Rate-Distortion')

plt.legend()
plt.show()