import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
import matplotlib.ticker as ticker

tick_spacing = 1.0


'''
#mobile
title = 'mobile cif' 
psnr_l1 = [21.3610, 24.2898, 27.1683, 29.8436, 32.5880, 35.8842]
psnr_l2 = [22.5860, 25.5810, 28.5750, 30.7199, 33.9017, 37.8781]
psnr_l3 = [24.2813, 27.1290, 29.3289, 31.5049, 34.7309, 38.8228]
psnr_l4 = [24.6169, 28.0420, 29.6636, 31.9278, 35.3221, 39.5869]
psnr_l5 = [24.8370, 28.3283, 29.8866, 32.1671, 35.5854, 39.8465]
psnr_l6 = [25.2754, 28.6743, 30.3215, 32.7524, 36.4155, 40.7555]

bitrate_l1 = [24.5660, 53.2580, 98.2160, 173.6420, 344.5160, 784.5100]
bitrate_l2 = [21.7520, 38.8360, 72.5580, 107.7120, 307.5100, 941.5760]
bitrate_l3 = [52.6720, 97.3580, 155.1380, 263.5720, 604.1200, 1469.7520]
bitrate_l4 = [50.1980, 94.4520, 115.7560, 198.8200, 531.4520, 1416.1100]
bitrate_l5 = [13.6540, 26.9300, 31.7120, 53.6100, 100.6840, 163.1520]
bitrate_l6 = [21.3440, 33.8840, 56.7660, 118.6560, 304.6680, 550.8060]
'''

#akiyo cif
title = 'akiyo_cif'
psnr_l1 = [ 29.4716, 32.2735, 35.1259, 37.9908, 40.7400, 43.3382]
psnr_l2 = [ 30.4634, 33.5273, 36.4065, 38.6974, 41.5055, 44.1473]
psnr_l3 = [ 32.2561, 35.1453, 37.4439, 39.6769, 42.3197, 44.8510]
psnr_l4 = [ 32.6374, 36.1168, 37.6765, 39.8217, 42.5727, 45.1306]
psnr_l5 = [ 32.7298, 36.2945, 37.8281, 40.1561, 42.8697, 45.3633]
psnr_l6 = [ 33.1123, 36.7152, 38.3358, 40.5661, 43.3760, 45.8748]

bitrate_l1 = [6.1800, 9.7520,  15.1160, 24.1300, 40.7560, 74.9300]
bitrate_l2 = [4.6720, 6.5140,  9.9060,  12.2140, 23.9280, 54.6020]
bitrate_l3 = [9.3040, 14.8260, 21.4140, 32.7100, 58.8640, 115.2540]
bitrate_l4 = [8.8560, 14.6000, 15.9780, 22.0480, 42.2960, 92.9900]
bitrate_l5 = [4.0160, 4.9920,  5.6180,  9.5560,  14.0340, 24.5260]
bitrate_l6 = [4.8920, 6.9000,  9.7280,  13.0520, 27.5520, 56.7980]

ssim_l1 = [0.831427, 0.888195, 0.927836, 0.953060, 0.968849, 0.978470]
ssim_l2 = [0.849727, 0.905153, 0.938138, 0.957613, 0.971847, 0.980412]
ssim_l3 = [0.887911, 0.927973, 0.949134, 0.963742, 0.975075, 0.982367]
ssim_l4 = [0.890922, 0.935488, 0.950299, 0.964106, 0.975882, 0.982834]
ssim_l5 = [0.891975, 0.937507, 0.951441, 0.965632, 0.976828, 0.983472]
ssim_l6 = [0.897939, 0.941711, 0.955233, 0.967758, 0.978327, 0.984808]

'''
#BigBuckBunny
title = 'BigBuckBunny_CIF'
psnr_l1 = [33.2307, 34.7037, 36.6861, 39.2522, 42.3551, 45.4873]
psnr_l2 = [33.6688, 35.6542, 37.7966, 40.0367, 43.2137, 46.5077]
psnr_l3 = [34.7050, 36.6882, 38.6176, 40.9235, 44.1805, 47.4706]
psnr_l4 = [35.0152, 37.4277, 38.8744, 41.3386, 44.5920, 47.8946] 
psnr_l5 = [35.1238, 37.7401, 39.2350, 41.7346, 44.9904, 48.2661]
psnr_l6 = [35.4047, 38.1602, 39.7951, 42.3807, 45.7821, 48.9399]

bitrate_l1 = [3.8960, 5.1800, 8.6160, 15.9700, 30.6580, 58.1820]
bitrate_l2 = [3.2220, 4.7460, 7.3080, 8.8300, 17.4180, 35.9040]
bitrate_l3 = [4.8020, 8.1320, 13.5620, 23.5520, 46.1340, 86.9000]
bitrate_l4 = [4.9920, 9.3160, 11.3200, 16.5320, 31.3080, 62.0640]
bitrate_l5 = [3.7940, 5.1280, 6.5320, 8.8340, 12.8100, 21.0880]
bitrate_l6 = [4.3880, 5.8740, 8.4100, 11.2620, 20.7980, 38.6300]
'''

bitrate_l1_sum = [0]*6
bitrate_l2_sum = [0]*6
bitrate_l3_sum = [0]*6
bitrate_l4_sum = [0]*6
bitrate_l5_sum = [0]*6
bitrate_l6_sum = [0]*6

for qp_set in range(0,6):
    bitrate_l1_sum[qp_set] = bitrate_l1[qp_set]
    bitrate_l2_sum[qp_set] = bitrate_l1_sum[qp_set] + bitrate_l2[qp_set]
    bitrate_l3_sum[qp_set] = bitrate_l2_sum[qp_set] + bitrate_l3[qp_set]
    bitrate_l4_sum[qp_set] = bitrate_l3_sum[qp_set] + bitrate_l4[qp_set]
    bitrate_l5_sum[qp_set] = bitrate_l4_sum[qp_set] + bitrate_l5[qp_set]
    bitrate_l6_sum[qp_set] = bitrate_l5_sum[qp_set] + bitrate_l6[qp_set]
    

#s = UnivariateSpline(x, y, s=5)
fig, plots = plt.subplots(2, 1)
#fig, bx = plt.subplots()
plots[0].plot(bitrate_l1_sum, psnr_l1, 'r', label='layer 1')#, marker='s')
plots[0].plot(bitrate_l2_sum, psnr_l2, 'b', label='layer 2')#, marker='s')
plots[0].plot(bitrate_l3_sum, psnr_l3, 'g', label='layer 3')#, marker='s')
plots[0].plot(bitrate_l4_sum, psnr_l4, 'm', label='layer 4')#, marker='s')
plots[0].plot(bitrate_l5_sum, psnr_l5, 'y', label='layer 5')#, marker='s')
plots[0].plot(bitrate_l6_sum, psnr_l6, 'k', label='layer 6')#, marker='s')
plots[0].grid()
#plt.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

plots[1].plot(bitrate_l1_sum, ssim_l1, 'r', label='layer 1')#, marker='s')
plots[1].plot(bitrate_l2_sum, ssim_l2, 'b', label='layer 2')#, marker='s')
plots[1].plot(bitrate_l3_sum, ssim_l3, 'g', label='layer 3')#, marker='s')
plots[1].plot(bitrate_l4_sum, ssim_l4, 'm', label='layer 4')#, marker='s')
plots[1].plot(bitrate_l5_sum, ssim_l5, 'y', label='layer 5')#, marker='s')
plots[1].plot(bitrate_l6_sum, ssim_l6, 'k', label='layer 6')#, marker='s')
plots[1].grid()

plots[0].set(xlabel='bitrate', ylabel='PSNR')
plots[1].set(xlabel='bitrate', ylabel='SSIM')
fig.suptitle('Rate-Distortion, ' + title)
#plt.axis([0, 6, 0, 20]) #xmin, xmax, ymin, ymax

plt.legend()
plt.show()


#---------------------------- bar plots -----------------------------# 
labels = ['BL', 'EL1', 'EL2', 'EL3', 'EL4', 'EL5']
akiyo = [17.1, 23.4 ,36.6, 44.5, 49.8, 54.3]
mobile = [790, 1186, 1800, 2037, 2150, 2249]
bigbuckbunny = [23, 25.1, 37.0, 44.3, 49.0, 52.9]

akiyo_values = [1, 1.37 , 2.14, 2.60, 2.91, 3.17]
mobile_values = [1, 1.5, 2.27, 2.57, 2.72, 2.84]
bigbuckbunny_values = [1, 1.1, 1.6, 1.7, 2.1, 2.3]

average_overhead = [0]*6

for i in range(0,6):
    average_overhead[i] = (akiyo_values[i] + mobile_values[i] + bigbuckbunny_values[i])/3.0

x = np.arange(len(labels)) 
width = 0.5  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x , average_overhead, width, label='avg. overhead')
'''
rects1 = ax.bar(x - width*3/4, akiyo_values, width, label='akiyo')
rects2 = ax.bar(x , mobile_values, width, label='mobile')
rects3 = ax.bar(x + width*3/4, bigbuckbunny_values, width, label='bigbuckbunny')
'''
ax.set_ylabel('Bitrate Overhead')
ax.set_title('Bitrate Overhead for Multiple Layers, 36dB')
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