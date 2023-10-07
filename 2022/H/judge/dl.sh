#!/bin/sh

links=$(curl -s "$1" | grep -o 'href="[^"]*\.in\|href="[^"]*\.ans' | sed 's/href="//;s|^|'"$1"'|')
IFS=$'\n'
for link in $links; do
  curl -O "$link"
done