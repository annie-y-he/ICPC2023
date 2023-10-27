#!/bin/sh

python ./*.py < in$1.txt > output.txt
dos2unix -q output.txt
diff output.txt out$1.txt
echo $?