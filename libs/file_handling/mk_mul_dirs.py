import os

dir_test = 'testdir/abhi/'
if not os.path.exists(dir_test):
    os.makedirs(dir_test)
else:
    print('the directory already exists.')