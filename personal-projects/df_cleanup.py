import os, time, shutil
# importing required modules
  
path = "${pwd}"
# setting path to current working directory
  
total, used, free = shutil.disk_usage(path)
# Disk usage statistics
# about the given path
  
total_2_dp = round(total / 2**30, 2)
used_2_dp = round(used / 2**30, 2)
free_2_dp = round(free / 2**30, 2)
# round to 2 decimal points

threshold = 80
# define threshold at which disk cleanup should be performed 

if (used / total)*100 >= threshold:
    print(total)
    # if disk usage is greater than or equal to threshold
    # run diskcleanup (placeholder set currently)

else: 
    print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")
    # otherwise, show disk usage in cli

log_path = r"/var/log"
 
# file modification
timestamp = os.path.getmtime(log_path)

days = 40

s_in_days = time.time() - (days * 24 * 60 * 60) 
# time.time() is current time relative to epoch => Jan 1st 1970 00:00:00 UTC
# minus 40 days in seconds

for file in os.listdir(log_path):
    
    filename = os.fsdecode(file)
    
    if timestamp >= s_in_days:
        os.remove(filename)

        break