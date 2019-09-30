import os, sys


path = "/Users/shiweizhi/Downloads/frames2/xbm"

files = os.listdir( path )

files.sort()


outfile = "/Users/shiweizhi/Downloads/frames2/xbm/gencode.txt"
outfile1 = "/Users/shiweizhi/Downloads/frames2/xbm/gencode1.txt"

fout = open(outfile, 'w')
fout1 = open(outfile1, 'w')

n = 1064

for i in range(1, n):
    f = open(path+'/'+files[i])
    a = f.read()
    a = a.replace("image_bits[]", "image_bits"+ str(i)+"[] PROGMEM ")
    a = a.split("image_height 50")
    a = a[1]

    fout.write(a)

    fout.writelines("")


for i in range(1, n):
    fout1.write("memcpy_P(buf, image_bits{}, len_xyz);\n".format(i))
    # fout1.write("u8g2.clearBuffer();\n")
    fout1.write("u8g2.drawXBM( 0, 0, u8g_logo_width, u8g_logo_height, buf);\n")
    fout1.write("u8g2.sendBuffer();\n")
    fout1.write("delay(d_time);\n")

    fout1.write("")







