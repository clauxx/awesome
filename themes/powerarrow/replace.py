import pandas as pd
import numpy as np

files = open('theme.lua', 'rb') 
lua_file = open('theme.test.lua', 'w')
lines = files.read().decode("utf-8").splitlines() 
files.close()

#data = np.genfromtxt('colors.csv', dtype=None, delimiter=',', names=False) 

data = pd.read_csv('colors.csv', header=None)
colors = np.array(data)[0]


for line in range(len(lines)):
    if(lines[line].endswith('findmeplease')):
        index = line
    elif(lines[line].endswith('findwallpaper')):
        index_w = line

lines[index] = 'local colors = {"' + colors[0] + '","' + colors[1] + '","' + colors[2] + '","' + colors[3] + '","' + colors[4] + '"} --findmeplease'

lines[index_w] = 'theme.wallpaper = theme.dir .. "/' + colors[5] + '" --findwallpaper'

theme = '\n'.join(lines)

lua_file.write(theme)
lua_file.close()


