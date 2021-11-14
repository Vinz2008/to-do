import os
directory = ".todo"
parent_dir = os.path.expanduser('~')
path = os.path.join(parent_dir, directory)
os.mkdir(path)
with open(path + '/todolist.txt', 'w') as f:
    f.write("")
