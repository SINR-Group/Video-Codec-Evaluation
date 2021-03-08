import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.ticker as ticker

tick_spacing = 1.0

#H265 - All 14 VTL sequqnces
#----------------Quality----------------
psnr_l0 = [26.98686153846154, 29.43374615384616, 31.92706923076923, 34.36793846153845, 36.84483076923077, 39.44556923076924]
psnr_l1 = [27.982653846153845, 30.579276923076918, 33.12213846153846, 35.12333846153847, 37.76731538461539, 40.66636153846154]
psnr_l2 = [29.43386923076923, 31.949638461538466, 33.90891538461538, 35.87237692307693, 38.46959230769231, 41.38698461538461]
psnr_l3 = [29.793938461538467, 32.7705, 34.1659923076923, 36.15764615384615, 38.8538076923077, 41.865684615384616]
psnr_l4 = [29.98139230769231, 32.98224615384615, 34.396369230769224, 36.44072307692308, 39.15071538461539, 42.18108461538462]
psnr_l5 = [30.322738461538464, 33.344853846153846, 34.798676923076926, 36.89297692307692, 39.73162307692308, 42.7749]

#----------------Bitrate----------------
bitrate_l0 = [9.043846153846152, 17.127384615384617, 32.19015384615384, 60.60092307692307, 123.46553846153847, 278.09015384615384]
bitrate_l1 = [16.976461538461535, 31.221538461538458, 59.21615384615384, 102.58661538461537, 232.2046153846154, 599.9727692307692]
bitrate_l2 = [33.72446153846153, 63.30707692307692, 112.91861538461538, 195.6913846153846, 441.75230769230774, 1126.1078461538461]
bitrate_l3 = [50.314923076923066, 97.62969230769231, 156.48984615384614, 269.0916923076923, 626.6143076923076, 1644.4483076923075]
bitrate_l4 = [56.283384615384605, 106.99061538461538, 168.6463076923077, 290.6956923076923, 670.0204615384615, 1746.555846153846]
bitrate_l5 = [64.33476923076923, 120.42999999999999, 189.178, 330.16061538461537, 771.9956923076923, 1975.9590769230767]

#-------------------------------PLOTS--------------------------------------

#fig, plots = plt.subplots(2, 1)
#fig, bx = plt.subplots()
plt.plot(bitrate_l0,  psnr_l0,  label='layer 1')#, marker='s')
plt.plot(bitrate_l1,  psnr_l1,  label='layer 2')#, marker='s')
plt.plot(bitrate_l2,  psnr_l2,  label='layer 3')#, marker='s')
plt.plot(bitrate_l3,  psnr_l3,  label='layer 4')#, marker='s')
plt.plot(bitrate_l4,  psnr_l4,  label='layer 5')#, marker='s')
plt.plot(bitrate_l5,  psnr_l5,  label='layer 6')#, marker='s')
plt.grid()
#plt.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plt.xlabel('bitrate')
plt.ylabel('PSNR')
plt.title("RD Plot, Multiple Layers, SHVC")
plt.legend()

plt.legend()
plt.show()

#---------------------------- bar plots -----------------------------# 
labels = ['BL', 'EL1', 'EL2', 'EL3', 'EL4', 'EL5']
#Quality = 36

bitrate_36dB = [102, 145 ,208, 260, 265, 270]
bitrate_overhead_36dB = [1, 1.42 , 2.03, 2.54, 2.60, 2.65]

#Quality = 40
bitrate_40dB = [354, 510 ,791, 881, 985, 1017]
bitrate_overhead_40dB = [1, 1.44 , 2.23, 2.48, 2.78, 2.87]

Quality = 32
bitrate = [33, 47 ,65, 86, 91, 95]
bitrate_overhead = [1, 1.42 , 1.97, 2.6, 2.75, 2.88]

x = np.arange(len(labels)) 
width = 0.5  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x , bitrate_overhead, width, label='avg. overhead')
'''
rects1 = ax.bar(x - width*3/4, akiyo_values, width, label='akiyo')
rects2 = ax.bar(x , mobile_values, width, label='mobile')
rects3 = ax.bar(x + width*3/4, bigbuckbunny_values, width, label='bigbuckbunny')
'''
ax.set_ylabel('Bitrate Overhead')
ax.set_title('Bitrate Overhead for Multiple Layers,' + str(Quality))
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{0:.3g}'.format(height),
                    xy=(rect.get_x() + rect.get_width(), height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

#autolabel(rects1)
autolabel(rects2)
#autolabel(rects3)
fig.tight_layout()
plt.show()