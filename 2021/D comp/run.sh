#!/bin/sh

python ./*.py < s$1.in > output.txt
dos2unix -q output.txt
diff output.txt s$1.ans
echo $?