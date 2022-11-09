import os
import shutil
from pathlib import Path
from time import sleep

def mk_dir(dir: str):
    try:
        os.mkdir(dir)
    except Exception as error:
        raise error

def rm_file(file: str):
    try:
        os.remove(file)
    except FileNotFoundError as error:
        pass

def next_file(dir):
    leng = len(os.listdir(dir))
    next = f'{leng + 1}'.rjust(4, '0')
    return next

def rearrange(dir):
        count = 0
        for file in sorted(os.listdir(dir)):
            count += 1
            suffix = Path(dir + file).suffix
            
            new_name = f'{count}'.rjust(4, '0')
            shutil.move(dir + file, dir + new_name + suffix)
          
        
if __name__ == "__main__":
    rearrange('tmp/working/')