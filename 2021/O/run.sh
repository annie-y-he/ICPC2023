#!/bin/sh

# python ./*.py < in$1.txt > output.txt
# diff output.txt out$1.txt

python ./*.py < a$1.in > output.txt
diff output.txt a$1.ans

echo $?