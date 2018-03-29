from colorthief import ColorThief
import sys
import numpy as np

if sys.argv[1]:
    color_thief = ColorThief(sys.argv[1])
    palette = color_thief.get_palette(color_count=6)
else:
    print('Select image please.')
    
colors = []
for color in range(len(palette)):
    hexes = '#%02x%02x%02x' % palette[color]
    colors.append(hexes)

colors = colors[:5]
colors.append(sys.argv[1])

files = open('theme.lua', 'rb') 
lua_file = open('theme.test.lua', 'w')
lines = files.read().decode("utf-8").splitlines() 

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


