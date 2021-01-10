#!/bin/bash

cwd=$(pwd)

while true
do
  inotifywait -e close_write /urban/uploads |
  while read -r date time dir file
  do
    changed_abs=${dir}${file}
    echo "At ${time} on ${date}, file $changed_abs" > ./logs.txt
  done
done
