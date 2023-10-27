#!/bin/sh

for infile in *.in; do
  base_name=$(basename "$infile" .in)
  python ../*.py < "$base_name.in" > "$base_name.txt"
  dos2unix -q "$base_name.txt"
  echo "diff $base_name: "
  diff "$base_name.txt" "$base_name.out"
  echo $?
done