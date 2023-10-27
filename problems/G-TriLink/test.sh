#!/bin/bash
for test in *.in; do
  name=$(basename "$test" .in)
  ./$q.py <"$name.in" >"$name.txt"
  echo "TEST $name: "
  cat "$name.txt"
  echo "DIFF $name: "
  diff "$name.txt" "$name.ans"
  echo $?
done
