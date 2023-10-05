#!/bin/sh

for i in $(seq 1 $1); do
  touch "in$i.txt"
  touch "out$i.txt"
done