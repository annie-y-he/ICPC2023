#!/bin/bash
for test in sample/*.in; do
  name=$(basename "$test" .in)
  echo "TEST $name: "
  ./B.py <"$name.in" >"$name.txt"
  cat "$name.txt"
  echo "DIFF $name: "
  diff "$name.txt" "$name.ans"
  echo $?
done
for test in sample/*.interaction; do
  name=$(basename "$test" .interaction)
  echo "TEST $name: "
  ./B.py <"$name.interaction"
done
