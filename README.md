# awesome

Change the wallpaper and the color palette of the powerarrow theme that matches the wallpaper

run the bash script wpchange.sh from /awesome/themes/powerarrow/ with the wallpaper argument

e.g. ./wpchange /wallpapers/space.jpg

Specific:
* the theme.lua file has the "--findmeplease" and "--findwallpaper" comments for the python script
* if it's a one color wallpaper, probably will fail and kill your theme.lua, so backup first!
* my backup works only if the script runs successfully

ToDo's:
* save wallpaper configs in the .csv file and be able to chose a specific color configuration
* make it more flexible smh (make it work with one color, which is easy -> modify the .php with some logic)
* put the scripts in a separate folder (files: color.php, colors.csv, replace.py, wpchange.sh)
* try a few more APIs, maybe some of them has a better output
* randomize the order of the colors in the powerarrow
