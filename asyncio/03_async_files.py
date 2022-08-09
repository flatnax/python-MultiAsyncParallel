import aiofiles

def read_large_file():
    with open('..\\data\\big_file.txt', r) as f:
        return f.read()

