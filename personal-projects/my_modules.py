import time, os, shutil

path = os.getcwd()

total, used, free = shutil.disk_usage(path)
# Disk usage statistics
# about the given path

total_2_dp = round(total / 2**30, 2)
used_2_dp = round(used / 2**30, 2)
free_2_dp = round(free / 2**30, 2)
# round to 2 decimal points

def dfcleanup():

    timestamp = os.path.getmtime(path)
    # return last modified time of file

    days = 40

    s_in_days = time.time() - (days * 24 * 60 * 60) 
    # time.time() is current time relative to epoch => Jan 1st 1970 00:00:00 UTC
    # minus 40 days in seconds

    for file in os.listdir(path):
        #ignore the following: (.os, .exe)
        filename = os.fsdecode(file)
        
        if timestamp >= s_in_days:
            os.remove(filename)

            break
