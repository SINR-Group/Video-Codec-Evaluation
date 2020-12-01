# Codec-Evaluation

### Codec-evaluation is a tool to encode/decode and measure quality of video sequences using ffmpeg codecs.

You can control -
1. What yuv sequence to encode/decode and measure quality, their resolution and framerate.
2. What video codec to use - currently supported H.264, H.265 and VP9.
3. What encode parameter to use - change the quality (crf), gop size, presets (fast, slow etc.)


Setting up env. before run -
1. Keep you yuv raw videos in the ./yuv_test_sequence folder, in corresponding resolution folder.
2. Update the config file, check the quality range, gop value, codec type etc.
3. Run evaluate.py


### Output 

#### Sample putput is shown below - 
psnr_avg_288_libx264 =  [26.29607773919204, 28.25003059852258, 30.81174368888136, 32.69310659791685, 34.63873376629648, 36.64967347023189, 38.76475614356222]

ssim_avg_288_libx264 =  [0.9641060906012429, 0.9781503071221932, 0.9881359175721655, 0.9921370460460665, 0.9947620193804771, 0.9964253007938786, 0.9975398672198192]

vma_avg_288_libx264 =  [68.98055665043144, 79.56509812560193, 89.95869716033334, 94.88849898346604, 97.20867335608702, 98.42591591777732, 99.14592374667019]

bpp_288_libx264 =  [0.01386311026936027, 0.01937605218855219, 0.031679555976430976, 0.0476701914983165, 0.07385890151515151, 0.11395412457912459, 0.17678766835016835]


### Plotting

The folder ./plotter has the script to plot rate-distortion graph.


### Requirements 

1. python3,  matplotlib
2. ffmpeg with lbvmaf

#### References 
1. https://ffmpeg.org/ - for ffmpeg usage
2. For linbmaf usage -  https://ffmpeg.org/ffmpeg-all.html#libvmaf for usage
3. For linbmaf installation - https://github.com/Netflix/vmaf
