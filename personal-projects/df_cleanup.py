#!/usr/bin/env python3

from my_modules import *
# importing required modules

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