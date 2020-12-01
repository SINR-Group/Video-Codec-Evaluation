import os, sys
sys.path.append(os.getcwd() + '/')
sys.path.append(os.getcwd() + '/codecs')
sys.path.append(os.getcwd() + '/scripts')

import glob
import configparser 
from runvp9 import runvp9
from runh26x import runh26x
from quality import quality
from average import average


class Evaluate():
    def __init__(self):
        self.parse_config()
        self.ret = []

    def parse_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
       
        #codec params
        self.preset_26x = config['CODEC']['preset_26x']
        self.preset_vpx = config['CODEC']['preset_vpx']
        self.codec      = config['CODEC']['codec']
        self.gop        = config['CODEC']['gop']
        self.crf        = config['CODEC']['crf']
           
        #Sequence
        self.frames     = config['SEQUENCE']['frames']
        self.fps        = config['SEQUENCE']['fps']
        self.width      = config['SEQUENCE']['width']
        self.height     = config['SEQUENCE']['height']
        self.num_seq    = config['SEQUENCE']['num_seq']
       
        #paths
        self.bin_out       = config['PATHS']['encode_out']
        self.results       = config['PATHS']['results']
        self.test_sequence = config['PATHS']['test_sequence']
        self.log_out       = config['PATHS']['log_out']
      
    def readfilename(self):
        files = glob.glob(self.test_sequence + self.height + '/*.yuv')
        for f in files:
            name = f.split('/')[-1]
            name = name.split(".")[0]
            self.ret.append(name)

    def cleanup(self):
       for f in glob.glob(self.bin_out + self.height + '/*.mp4'):
           os.remove(f)

       for f in glob.glob(self.results + self.height + '/*.json'):
           os.remove(f)
      
       for f in glob.glob(self.log_out + self.height + '/*.log'):
            os.remove(f)

    def encode_decode(self):
        if self.codec == 'libvpx-vp9':
            runvp9(self)
        else:
            runh26x(self)
    
    def measure_quality(self):
        quality(self)

    def average_all_sequence(self):
        average(self)


if __name__ == '__main__':
    eval = Evaluate()
    eval.cleanup()
    eval.encode_decode()
    eval.measure_quality()
    eval.average_all_sequence()
