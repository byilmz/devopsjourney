     
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

print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")
# show disk usage in cli