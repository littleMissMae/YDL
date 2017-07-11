import youtube_dl
import sys, os

#Read urls into a list
def make_list(filename):
    print("Reading List")
    f = open(filename)
    l = [l for l in f.readlines() if l.strip()]
    f.close()
    url_list = l 
    return url_list
   

#Create directory and file path
def make_dir(dir_name):
    dir_path = "/home/emer/Media/Music/" + dir_name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        os.chdir(dir_path)
        print(dir_name + " created")
    else:
        print("Addining to Directory " + dir_name)
        os.chdir(dir_path)
    return dir_path


#Download each url
def download_list(url_list):
    mode = input("Download " + sys.argv[1] + " into " + sys.argv[2] + " y/n?")
    if mode == "y":
        ydl_opts={}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for u in url_list:
                ydl.download([u])
    else:
        print("Operation Cancelled")
        sys.exit

#Neaten filename
def clean_filename(dirname):
    path = '/home/emer/Media/Music/'+dirname
    print("Cleaning file names")
    for filename in os.listdir(path):
        if filename.endswith('.mp3'):
            i = filename.rfind('-')
            newname = filename[:i]
            os.rename(os.path.join(path,filename), os.path.join(path, newname))
    print('Download Completed')

#Remove textfile
def remove_file(filename):
    mode = input("would you like to remove the list? y/n")
    if mode == 'y':
        path = os.path.realpath(filename)
        os.remove(path)

url_list = make_list(sys.argv[1])
make_dir(sys.argv[2])
download_list(url_list)
clean_filename(sys.argv[2])

