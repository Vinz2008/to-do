import os
directory = ".todo"
parent_dir = "~"
path = os.path.join(parent_dir, directory)
os.mkdir(path,mode = 0o666)
with open('~/.todo/todolist.txt', 'w') as f:
    f.write("")
