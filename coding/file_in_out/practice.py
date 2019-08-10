import os
"""
- dirpath: name of the current folder
- dirnames: A list of folders in the current folder
- files: A list of files in the current folder
"""
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    print(f'Found dirname: {dirnames}')
    print('\n')
    for file in files:
        print(file)