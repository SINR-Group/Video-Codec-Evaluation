import os, glob, sys

source_width = 3840
source_height = 2160
target_width = 1920
target_height = 1080 #1920x1080, 1280x720, 854x480, 352 x 288, 640x360

'''Beauty_1920x1080_120fps_420_8bit_YUV_RAW'''
def readfilename(path):
    ret = []
    files = glob.glob(path + '/*.yuv')
    for f in files:
        name = f.split('/')[-1]
        ret.append(name)
    return ret


def resize():
    '''ffmpeg -s:v 1920x1080 -r 25 -i input.yuv -vf scale=960:540 -c:v rawvideo -pix_fmt yuv420p out.yuv'''    
    input_path  = './' + str(source_height) + '/'
    output_path = './' + str(target_height) + '/'
   
    for f in glob.glob(output_path + '*.yuv'):
        os.remove(f)
   
    sequence_list = readfilename(input_path)
   
    for seq in sequence_list:
         infile = input_path + seq
         
         out_split = seq.split('_')
         out_split[1] = str(target_width) + 'x' + str(target_height)
         out = "_".join(out_split)
         outfile = output_path + out + '.yuv'

         command =  'sudo ffmpeg -s:v ' + str(source_width) + 'x' + str(source_height) + ' -r 120 '
         command += ' -i ' + infile + ' -vf scale=' + str(target_width) + ':' + str(target_height)
         command += ' -c:v rawvideo -pix_fmt yuv420p ' +  outfile

         print(command + '\n')
         os.system(command)


if __name__ == '__main__':
    resize()

