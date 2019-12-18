import os

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

        with open(path, 'rb') as f:
            bitmaps[path] = f.read()  # returns 'bytes' object

    print('Bytes: ', bitmaps)  # file1: bytes, file2: bytes ...

    # bitmaps values are 'bytes' now.
    # To be able to do | and & we have to transform them to integers

    for file, file_bytes in bitmaps.items():
        bitmaps[file] = int.from_bytes(file_bytes, byteorder='big')

    print('Integers: ', bitmaps)  # file1: int, file2: int ...

    # Let's do | now
    accumulator = 0

    for file_bytes in bitmaps.values():
        accumulator |= file_bytes

    print('Accumulator int: ', accumulator)

    # To iterate over bits we can use built-in 'bin'.
    # It returns a string containing '1' and '0'.
    bits = bin(accumulator)[2:]  # cut the binary prefix, we need the bits only

    print('Bits: ', bits)

    # let's iterate over the bits
    for bit in bits:
        if bit == '1':
            pass
        else:
            pass

    # Now let's open a binary file and iterate over its bytes and over the bits

    with open(TEST_FILE, 'rb') as test_file:
        for byte, bit in zip(test_file.read(), bits):
            print('Byte - bit: ', byte, bit)


if __name__ == '__main__':
    main()
