# alpine used as base docker image as it is a lightweight linux distribution
# alpine shrinks the docker image so it uses significantly less space and is faster
FROM python:3.7-alpine

# set the working directory
WORKDIR /usr/local/bin

# copy file from source (same directory)
# period "." indicates the dockerfile exists in the same directory as source file
COPY df_cleanup.py .

# command to run the clean up script
CMD ["python3", "df_cleanup.py"]