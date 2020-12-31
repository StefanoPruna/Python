#With this program we visualize all the directories in the folder

import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isdir(path):
            walk(path)
        else:
            print(path)

walk(os.getcwd())