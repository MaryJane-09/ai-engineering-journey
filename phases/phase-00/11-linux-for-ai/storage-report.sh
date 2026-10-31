#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path1> [path2] [path3] ..." >&2
    exit 1
fi

for path in "$@"; do
    if [ -e "$path" ]; then
        du -sh "$path"
    else
        echo "Error: '$path' does not exist." >&2
    fi
done
