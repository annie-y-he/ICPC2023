#!/bin/bash
for ino in ./*; do
  echo $ino
  if [ -d "$ino" ]; then
    dir=$(basename "$ino")
    q="${dir:0:1}"
    echo "#!/usr/bin/python3" >"$ino/$q.py"
    chmod 777 "$ino/$q.py"
cat >>"$ino/test.sh" <<EOF
#!/bin/bash
for test in *.in; do
  name=\$(basename "\$test" .in)
  ./\$q.py <"\$name.in" >"\$name.txt"
  echo "TEST \$name: "
  cat "\$name.txt"
  echo "DIFF \$name: "
  diff "\$name.txt" "\$name.ans"
  echo \$?
done
EOF
    chmod 777 "$ino/test.sh"
cat >>"$ino/Makefile" <<EOF
test:
\t./test.sh
run:
\t./$p.py
pdf:
\tevince $dir.pdf
EOF
  fi
done
