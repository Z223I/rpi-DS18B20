import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


device_folders = glob.glob(base_dir + '28*')

device_files = []
for xfolder in device_folders:
    device_files.append( xfolder + '/w1_slave' )


#for therm in device_files:
#    print therm

print "Number of thermometers: ", len(device_files)

device_file = base_dir + device_files[0] + "/w1_slave"
device_file = device_files[0]



def read_temp_raw(_device_file):
    f = open(_device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(_device_file):
    lines = read_temp_raw(_device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while True:
	#print(read_temp())

        for temperatureFile in device_files:
            print( read_temp( temperatureFile ) )

        print
	time.sleep(1)