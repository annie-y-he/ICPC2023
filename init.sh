#!/bin/sh

for dir in $(seq 65 $(printf '%d\n' "'$1")); do
  c="$(printf "\\$(printf '%03o' "$dir")")"
  mkdir "$c"
  touch "$c/$c.py"
  cp mk.sh "$c/mk.sh"
  cp run.sh "$c/run.sh"
done
