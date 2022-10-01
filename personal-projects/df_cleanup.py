#!/usr/bin/env python3

from my_modules import dfcleanup, clean_up_message
import shutil, os
# importing required modules
  
path = os.getcwd()
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
    dfcleanup()
    print("Clean up complete (:")
    print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")
    #alert smtp && rundiskcleanup
    # if disk usage is greater than or equal to threshold

else: 
    clean_up_message()
    print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")
    # otherwise, show disk usage in cli