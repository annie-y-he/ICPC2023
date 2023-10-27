#!/bin/sh

# Get the base URL without the last path
base_url=$(echo "$1" | awk 'BEGIN{FS=OFS="/"}{$NF=""; print $0}')

# Extract all PDF links
links=$(curl -s "$1" | grep -o 'href="[^"]*\.pdf' | sed 's/href="//')

# Download each link
for link in $links; do
  # Check if the link is relative. If yes, prepend the base URL
  link="$base_url$link"
  curl -O "$link"
done
