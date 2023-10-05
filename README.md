1. mk.sh
```bash
#!/bin/sh

for i in $(seq 1 $1); do
  touch "in$i.txt"
  touch "out$i.txt"
done
```
`./mk.sh 3`  
creates 3 sets of in/out txt files

2. run.sh
```bash
#!/bin/sh

python ./*.py < in$1.txt > output.txt
diff output.txt out$1.txt
echo $?
```
`./run.sh 1`  
runs test case 1 and give diff result

3. init.sh
```bash
#!/bin/sh

for dir in $(seq 65 $(printf '%d\n' "'$1")); do
  c="$(printf "\\$(printf '%03o' "$dir")")"
  mkdir "$c"
  touch "$c/$c.py"
  cp mk.sh "$c/mk.sh"
  cp run.sh "$c/run.sh"
done
```
`./init.sh O`  
creates folders from A to O with A.py and copies mk.sh and run.sh

**TIPS**
------------------
- Analyze time complexity. According to given range, given time limit and memory limit, maximize loop if necessary
