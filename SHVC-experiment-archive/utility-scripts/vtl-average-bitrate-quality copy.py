import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.ticker as ticker

tick_spacing = 1.0

#H264
psnr_h264 = [34.347141, 36.72672276923077, 38.62359276923076, 41.74466707692308] #[28.83665861538462, 32.14309938461538, 
ssim_h264 = [0.9791605384615385, 0.9876252307692309, 0.9918849230769232, 0.9957483076923078] #[0.9320049230769231, 0.9665745384615386, 
bitrate_h264 =  [0.04004097465034965, 0.07775125048562549, 0.13408459595959596, 0.33455686674436674] #[0.009870520104895105, 0.022154477466977466,

#H265
psnr_h265 = [30.567236230769232, 33.16145707692308, 35.811361769230764, 38.63666146153846] #[26.98686153846154, 29.43374615384616, 
ssim_h265 = [0.95409, 0.9735796923076924, 0.9851795384615385, 0.9919362307692309] #[0.8583956153846154, 0.9195916923076924, 
#bitrate_h265 = [0.05430743735431236, 0.07644103292540792, 0.1035669798951049, 0.15919452942890444, 0.3335297081390831, 0.8085784527972028]

bitrate_h265_kbps = [32.19015384615384, 60.60092307692307, 123.46553846153847, 278.09015384615384] #[9.043846153846152, 17.127384615384617, 
bitrate_h265 = []
for br in bitrate_h265_kbps:
    val = (br * 1000)/(25 * 352 * 288)
    bitrate_h265.append(val) 

#H266
psnr_h266    = [35.73730353846154, 37.7456303076923, 39.44001569230769, 42.09590176923078] #[30.81266746153846, 35.65835215384615, 
ssim_h266 = [0.9844378461538461, 0.9899640000000001, 0.9930310769230771, 0.995947769230769] #[0.9538790000000001, 0.9756127692307694, 
bitrate_h266 = [0.037862640831390834, 0.06634645736208236, 0.1083403141996892, 0.24479895104895105] #[0.010867873445998447, 0.022148710664335665, 

#-------------------------------PLOTS--------------------------------------

fig, plots = plt.subplots(2, 1)
#fig, bx = plt.subplots()
plots[0].plot(bitrate_h264,  psnr_h264,  'r', label='H264')#, marker='s')
plots[0].plot(bitrate_h265,  psnr_h265,  'b', label='H265')#, marker='s')
plots[0].plot(bitrate_h266,  psnr_h266,  'g', label='H266')#, marker='s')
plots[0].grid()
#plots[0].set_title('RD Plot, PSNR')
#plt.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plots[1].plot(bitrate_h264, ssim_h264, 'r', label='H264')#, marker='s')
plots[1].plot(bitrate_h265, ssim_h265, 'b', label='H265')#, marker='s')
plots[1].plot(bitrate_h266, ssim_h266, 'g', label='H266')#, marker='s')
plots[1].grid()
#plots[1].set_title('RD Plot, SSIM')


plots[0].set(xlabel='bits per pixel', ylabel='PSNR')
plots[1].set(xlabel='bits per pixel', ylabel='MS-SSIM')
fig.suptitle('Rate-Distortion')

plt.legend()
plt.show()