#!/bin/sh
set -euo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

git diff --cached --numstat --diff-filter=AM |
  sed '/-\t-\t/d;s/[0-9]\+\t[0-9]\+\t//' |
  while read -r file; do
    tmpfile="$(mktemp)"
    sed '1s/^\xef\xbb\xbf//;s/[ \t]*$//' "$file" | sed ':a;/^\n*$/{$d;N;ba}' > "$tmpfile"
    if cmp -s "$file" "$tmpfile"; then
      rm -f "$tmpfile"
    else
      mv "$tmpfile" "$file"
      echo "$file"
    fi
  done
