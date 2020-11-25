import os
import time


def litter(path):
    dirlist = os.listdir(path)
    print(dirlist)
    with open("nothing.txt", "w") as filepath:
        pass

    dirlist = os.listdir(path)
    print(dirlist)


def cleanup(path):
    dirlist = os.listdir(path)
    print(dirlist)
    file = "nothing.txt"
    location = path
    complete_path = os.path.join(location, file)
    os.remove(complete_path)
    dirlist = os.listdir(path)
    print(dirlist)


litter(path)
time.sleep(5)
cleanup(path)
