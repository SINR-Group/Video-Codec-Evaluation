import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.ticker as ticker

tick_spacing = 1.0

#H264
psnr_h264 = [32.14301014285714, 35.14013057142857, 37.14948957142857, 39.20759371428572, 40.70296642857143, 42.866887857142856]
ssim_h264 = [0.8648702857142857, 0.9039341428571429, 0.9261677142857143, 0.9444484285714286, 0.9547442857142857, 0.9664648571428572]
bitrate_h264 = [0.004976317239858906, 0.011199239417989419, 0.020922145061728396, 0.04085337301587302, 0.06842236552028219, 0.17879602072310405]

#H265
psnr_h265 = []
ssim_h265 = []
bitrate_h265 = []

bitrate_h265_kbps = []
bitrate_h265 = []
for br in bitrate_h265_kbps:
    val = (br * 1000)/(25 * 352*288)
    bitrate_h265.append(val) 

#H266
psnr_h266    = [34.52582128571429, 37.050027428571426, 38.78057428571429, 40.404796142857144, 41.672845571428574, 43.448876142857145]
ssim_h266    = [0.8970604285714286, 0.9249135714285713, 0.9406807142857142, 0.9528745714285713, 0.9604255714285713, 0.9690277142857143]
bitrate_h266 = [0.0036123567019400353, 0.00853355930335097, 0.016237147266313933, 0.030618441358024693, 0.052219240520282185, 0.13002317019400353]

#-------------------------------PLOTS--------------------------------------

fig, plots = plt.subplots(2, 1)
#fig, bx = plt.subplots()
plots[0].plot(bitrate_h264,  psnr_h264,  'r', label='H264')#, marker='s')
#plots[0].plot(bitrate_h265,  psnr_h265,  'b', label='H265')#, marker='s')
plots[0].plot(bitrate_h266,  psnr_h266,  'g', label='H266')#, marker='s')
plots[0].grid()
plots[0].set_title('RD Plot, PSNR')
#plt.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plots[1].plot(bitrate_h264, ssim_h264, 'r', label='H264')#, marker='s')
#plots[1].plot(bitrate_h265, ssim_h265, 'b', label='H265')#, marker='s')
plots[1].plot(bitrate_h266, ssim_h266, 'g', label='H266')#, marker='s')
plots[1].grid()
plots[1].set_title('RD Plot, SSIM')


plots[0].set(xlabel='bits per pixel', ylabel='PSNR')
plots[1].set(xlabel='bits per pixel', ylabel='SSIM')
fig.suptitle('Rate-Distortion')

plt.legend()
plt.show()