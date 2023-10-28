#!/bin/bash
for test in *.in; do
  name=$(basename "$test" .in)
  echo "TEST $name: "
  ./D.py <"$name.in" >"$name.txt"
  cat "$name.txt"
  echo "DIFF $name: "
  diff "$name.txt" "$name.ans"
  echo $?
done
for test in *.interaction; do
  name=$(basename "$test" .interaction)
  echo "TEST $name: "
  ./D.py <"$name.interaction"
done
