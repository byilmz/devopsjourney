     
import shutil
# importing required modules
  
path = "/home/burak/DevOps"
# defining necessary path
  
total, used, free = shutil.disk_usage(path)
# Disk usage statistics
# about the given path
  
total_2_dp = round(total, 2) # this doesn't work
print(type(total_2_dp))
print(f"Disk Usage:\nTotal: {total_2_dp / 2**30} GiB, Used:{used / 2**30} GiB, Free:{free / 2**30} GiB")
# show disk usage in cli


