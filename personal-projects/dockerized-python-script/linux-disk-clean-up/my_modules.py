# import required modules
import time, os, shutil

# define directory path
path = "/tmp"

# disk usage statistics
# about the given path
total, used, free = shutil.disk_usage(path)

# round to 2 decimal points
total_2_dp = round(total / 2**30, 2)
used_2_dp = round(used / 2**30, 2)
free_2_dp = round(free / 2**30, 2)

def dfcleanup():

    # return last modified time of file
    timestamp = os.path.getmtime(path)
    
    days = 40

    # time.time() is current time relative to epoch => Jan 1st 1970 00:00:00 UTC
    # minus 40 days in seconds
    s_in_days = time.time() - (days * 24 * 60 * 60) 

    for file in os.listdir(path):
        filepath = path+"/"+file
        
        # if last modified file date is >= 40 days
        # remove file
        if timestamp >= s_in_days:
                os.remove(filepath)

                break
