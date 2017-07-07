import glob, os, sys

def clean():
    path = '/home/emer/Media/Music/Junip'
    for filename in os.listdir(path):
        print(filename)
        if filename.endswith('.mp3'):
            newname = filename[:filename.index('-')]
            print(newname)
            os.rename(os.path.join(path,filename), os.path.join(path, newname)


