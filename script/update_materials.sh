#!/bin/bash
echo Update materials called with $1 $2
#$1 - temp dir
#$2 - target dir
rm -rf "$1"
mkdir -p "$1"
/var/www/materials/script/create_materials_tree.py "$1"
rsync --partial -avrpl --delete "$1"/ "$2"
chown -R root:materials "$2"
