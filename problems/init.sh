#!/bin/bash
for ino in ./*; do
  echo $ino
  if [ -d "$ino" ]; then
    dir=$(basename "$ino")
    q="${dir:0:1}"
    echo "#!/usr/bin/python3" >"$ino/$q.py"
    chmod 777 "$ino/$q.py"
    rm "$ino/test.sh"
cat >>"$ino/test.sh" <<EOF
#!/bin/bash
for test in *.in; do
  name=\$(basename "\$test" .in)
  echo "TEST \$name: "
  ./$q.py <"\$name.in" >"\$name.txt"
  cat "\$name.txt"
  echo "DIFF \$name: "
  diff "\$name.txt" "\$name.ans"
  echo \$?
done
for test in *.interaction; do
  name=\$(basename "\$test" .interaction)
  echo "TEST \$name: "
  ./$q.py <"\$name.interaction"
done
EOF
    chmod 777 "$ino/test.sh"
    rm "$ino/Makefile"
cat >>"$ino/Makefile" <<EOF
test:
	./test.sh
run:
	./$q.py
pdf:
	evince $dir.pdf
EOF
  fi
done
