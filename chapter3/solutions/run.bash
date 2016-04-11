#!/bin/bash

for file in `ls *.py`; do
    filename=$(basename $file)
    filename="${filename%.*}"
    python3 $filename.py < inputs/$filename.input

    if [[ $? != 0 ]]; then
        echo "Something failed"
        exit 1
    fi
done
