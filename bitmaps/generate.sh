#!/usr/bin/env sh

i=10; while [ $i -lt 42 ]; do echo -en '\x'$(printf "%0x" $i)''  >> binary.bm; i=$((i+1));  done
echo 'File 1'
xxd -b binary.bm

echo 'File 2'
i=42; while [ $i -gt 10 ]; do echo -en '\x'$(printf "%0x" $i)''  >> binary2.bm; i=$((i-1));  done
xxd -b binary2.bm
