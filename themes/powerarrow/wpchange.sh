#!/bin/bash

image=$1

python "kmeans.py" "$image"
echo "Processing image ..."
sudo mv "theme.lua" "theme.backup.lua"
sudo mv "theme.backup.lua" "/backup_themes"
sudo mv "theme.test.lua" "theme.lua"
echo "Done. Click {CTRL + Super + r}"


