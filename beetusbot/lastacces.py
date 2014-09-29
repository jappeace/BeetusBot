import os

CACHE_FILE = "latest.txt"

def get_latest():
    if ( not os.path.exists(CACHE_FILE)):
        open(CACHE_FILE, "w").close() #create the file
    with open(CACHE_FILE) as f:
        return f.readline() #closing is overrated

def set_latest(reddit_id):
    with open(CACHE_FILE, "w") as f:
        f.write(reddit_id)

