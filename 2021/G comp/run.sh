#!/bin/sh

python ./*.py < in$1.txt > output.txt
diff output.txt out$1.txt
echo $?