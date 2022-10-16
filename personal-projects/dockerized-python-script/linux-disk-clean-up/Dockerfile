FROM ubuntu:latest

# copy file from source to destination path
ADD requirements.txt .

# install dependencies
RUN apt-get update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y tcl
RUN apt install -y python3.8

# using pip package manager to install dependencies specified in requirements.txt
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt

# copy file from source to destination path
# period "." indicates the dockerfile exists in the same directory as source file
ADD df_cleanup.py .

ADD my_modules.py .

ADD clean_up_msg.py .

# command to run the clean up script
CMD ["python3", "./df_cleanup.py"]
