import os, requests, time

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

def clean_up_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbc348834299148cda800650e65554426.mailgun.org/messages",
        auth=("api", "72f0b060e1e5d58ea84677479ffe14b6-4534758e-30b9fa9b"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxbc348834299148cda800650e65554426.mailgun.org>",
            "to": "Burak Yilmaz <beeyilmaz46@gmail.com>",
            "subject": "Disk clean-up complete",
            "text": print(f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")})
