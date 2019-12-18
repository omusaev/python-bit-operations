#!/usr/bin/env sh

i=0; while [ $i -lt 256 ]; do echo -en '\x'$(printf "%0x" $i)''  >> binary.bm; i=$((i+1));  done
echo 'File 1'
xxd -b binary.bm

echo 'File 2'
i=256; while [ $i -gt 0 ]; do echo -en '\x'$(printf "%0x" $i)''  >> binary2.bm; i=$((i-1));  done
xxd -b binary2.bm
