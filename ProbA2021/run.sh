#!/bin/sh

python ./*.py < f$1.in > output.txt
diff output.txt f$1.ans

# python ./*.py < in$1.txt > output.txt
# diff output.txt out$1.txt
echo $?