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

def listFiles(base, suffix):
    assert os.path.isdir(base)
    for file in os.listdir(base):
        path = os.path.join(base, file)
        if path.endswith(suffix):
            print(path)
        if os.path.isdir(path):
            listFiles(path, suffix)

listFiles(os.getcwd(), os.getcwd())