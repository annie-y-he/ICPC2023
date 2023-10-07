#!/bin/sh

for infile in *.in; do
  base_name=$(basename "$infile" .in)
  python ../*.py < "$infile" > output.txt
  dos2unix -q output.txt
  echo "$base_name"
  diff output.txt "$base_name.ans"
  echo $?
done

rm output.txt