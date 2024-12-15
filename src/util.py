import os
import sys
import shutil

import generate

def copy_tree(source, destination):
    if not os.path.exists(source):
        print('source does not exist')
        sys.exit(-1)
    
    # delete destination contents if exists, and recreate directory
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    # copy source
    for item in os.listdir(source):
        src_item = os.path.join(source, item)
        dest_item = os.path.join(destination, item)

        if os.path.isfile(src_item):
            print(f'copying from {src_item}')
            print(f'copying to {dest_item}')
            shutil.copy(src_item,dest_item)
        else:
            # recursive directory call
            copy_tree(src_item, dest_item)

