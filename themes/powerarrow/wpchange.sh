#!/bin/bash

image=$1

php "color.php" "$image"
python "replace.py"
sudo mv "theme.lua" "theme.backup.lua"
sudo mv "theme.backup.lua" "/backup_themes"
sudo mv "theme.test.lua" "theme.lua"

