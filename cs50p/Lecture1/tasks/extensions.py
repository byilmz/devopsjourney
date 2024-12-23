ask_file = input("File name: ")
if ask_file.endswith(".gif"):
    print("image/gif")
elif ask_file.endswith(".jpg"):
    print("image/jpeg")
elif ask_file.endswith(".png"):
    print("image/png")
elif ask_file.endswith(".pdf"):
    print("application/pdf")
elif ask_file.endswith(".txt"):
    print("text/plain")
elif ask_file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
