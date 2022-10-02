# alpine used as base docker image as it is a lightweight linux distribution
# alpine shrinks the docker image so it uses significantly less space and is faster
FROM python:3.7-alpine

# set the working directory
WORKDIR /usr/local/bin

# copy file from source to destination path
ADD requirements.txt .

# using pip package manager to install dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# copy file from source to destination path
# period "." indicates the dockerfile exists in the same directory as source file
ADD df_cleanup.py .

ADD my_modules.py .

ADD clean_up_msg.py .

# command to run the clean up script
CMD ["python3", "df_cleanup.py"]