# https://bitstring.readthedocs.io/en/latest/

import functools
import operator
import os

from bitstring import Bits

BITMAPS_DIR = './bitmaps'
BITMAP_EXT = '.bm'
TEST_FILE = 'test.bin'


def main():

    bitmaps = {}

    # let's go over the files in the directory and put the binary data into the
    # dict
    for file in os.listdir(BITMAPS_DIR):
        if not file.endswith(BITMAP_EXT):
            continue
        path = os.path.join(BITMAPS_DIR, file)

        bitmaps[path] = Bits(filename=path)

    print('Bitstrings: ', bitmaps)  # file1: bytes, file2: bytes ...

    for file, bits in bitmaps.items():
        print(file)
        print(bits.bin)

    # same as 'a | b'
    accumulator = functools.reduce(operator.ior, bitmaps.values())
    print('Accumulator: ')
    print(accumulator.bin)

    # let's iterate over bits
    for bit in accumulator:
        print(bit)

    # Now let's open a binary file and iterate over its bytes and over the bits
    with open(TEST_FILE, 'rb') as test_file:
        for byte, bit in zip(test_file.read(), accumulator):
            if bit is True:
                print('+ Byte - bit: ', byte, bit)
            elif bit is False:
                print('- Byte - bit: ', byte, bit)


if __name__ == '__main__':
    main()
