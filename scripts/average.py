import glob
import os
import sys
import json


def readfilename(self):
    ret = []
    files = glob.glob(self.results + self.height + '/*.json')
    for f in files:
        name = f.split('/')[-1]
        ret.append(name)
    return ret


def crflist(crf):
    ret = []
    for q in crf.split(','):
        ret.append("_" + q + "_")
    ret.reverse()    
    return ret


def calc_avg_qual(self, crf_list, files):
    psnr_avg = []
    ssim_avg = []
    vmaf_avg = []
    
    height = self.height
    codec = self.codec
    result_path = self.results + height + '/'
    num_seq = int(self.num_seq)

    for crf in crf_list: #qp_set
        sum_ssim = 0
        sum_psnr = 0
        sum_vmaf = 0
        for res in files:
            if crf in res:
                with open(result_path + res, "r") as f1:
                        data = json.load(f1)
                        sum_ssim += data['MS-SSIM score']
                        sum_psnr += data['PSNR score']
                        sum_vmaf += data['VMAF score']
        
        psnr_avg.append(sum_psnr/(num_seq))
        ssim_avg.append(sum_ssim/(num_seq))
        vmaf_avg.append(sum_vmaf/(num_seq))

    print('psnr_avg_' + height + '_' + codec + ' = ', psnr_avg)
    print('ssim_avg_' + height + '_' + codec + ' = ', ssim_avg)
    print('vma_avg_'  + height + '_' + codec + ' = ', vmaf_avg)


def calc_avg_bpp(self, crf_list, files):
    size_avg   = []
    
    height  = self.height
    width   = self.width
    frames  = self.frames
    num_seq = self.num_seq
    codec   = self.codec
   
    path = self.bin_out + height + '/'

    for crf in crf_list:
        bitsum = 0.0
        for res in files:
            res = res.split('.')[0] + '.mp4'
            if crf in res:
                mp4 = path + res
                size = os.stat(mp4).st_size
                bitsum += (size*8.0)
        size_avg.append(bitsum/(int(num_seq) * int(width) * int(height) * int(frames)))
    
    print('bpp_' + height + '_' + codec + ' = ', size_avg)


def average(self):
    if self.mode == 'crf':
        crf = crflist(self.crf)
    else:
        crf = crflist(self.cbr)
    files = readfilename(self)
    calc_avg_qual(self, crf, files)
    calc_avg_bpp(self, crf, files)
