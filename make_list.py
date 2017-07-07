def make_list(filename):
    f = open(filename)
    l = [l for l in f.readlines() if l.strip()]
    f.close
    print(l)
    url_list = l 
    print(url_list)
    return url_list

make_list('tracks')
