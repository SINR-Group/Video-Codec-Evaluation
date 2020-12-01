import os
import glob
import sys

def readfilename(path):
    ret = []
    files = glob.glob(path + '/*.mp4')
    for f in files:
        name = f.split('/')[-1]
        ret.append(name)
    return ret


def quality(self):
    height = self.height
    width = self.width
    rate = self.fps
    frames = self.frames
    
    ref_path = self.test_sequence + height + '/'
    bin_out_path = self.bin_out + height + '/'
    result_path = self.results + height + '/'
    
    sequence_list = readfilename(bin_out_path)
   
    for sequence in sequence_list:
        '''
        ffmpeg -i main.mpg -i ref.mpg -lavfi libvmaf="psnr=1:log_fmt=json" -f null - > out.json

        ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -t 3 -i yuv_squence_cif/mobile_cif.yuv -i
        temp.mp4 -lavfi "ssim=ssim.log;[0:v][1:v]psnr=psnr.log" -f null -

        '''
        coded_sequence = sequence.split('_')
        main = sequence
        ref = "_".join(coded_sequence[:-3])
        ref = ref + '.yuv'
        out = main + '.json'

        
        command =  'sudo ffmpeg -i ' + bin_out_path + main 
        command += ' -f rawvideo -pix_fmt yuv420p -s:v ' + width + 'x' + height + ' -r ' + rate
        command += ' -i ' + ref_path + ref + ' -frames:v ' + frames + " " + ' -lavfi '
        command += 'libvmaf="psnr=1:ms_ssim=1:log_fmt=json:log_path=' + result_path + out + '" -f null - > '
        command += result_path + out
        print(command + '\n')
        os.system(command)

