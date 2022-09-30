     
import shutil
# importing required modules
  
path = "/home/burak/DevOps"
# defining necessary path
  
total, used, free = shutil.disk_usage(path)
# Disk usage statistics
# about the given path
  
total_2_dp = round(total / 2**30, 2)
used_2_dp = round(used / 2**30, 2)
free_2_dp = round(free / 2**30, 2)
# round to 2 decimal points

threshold = 80


if (used / total)*100 >= threshold:
    print(total)
    # if disk usage is greater than or equal to 80%
    # run diskcleanup (placeholder set currently)

else: 
    print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")
    # otherwise, show disk usage in cli
   
