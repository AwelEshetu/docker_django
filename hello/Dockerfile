#get base image from python 
FROM python:3
#set non buffered environment
ENV PYTHONUNBUFFERED=1
#make dir called code
RUN mkdir /code
#switch to code as working directory
WORKDIR /code
#copy requirements file to current /code/ directory
COPY requirements.txt /code/
#run pip install to install all requirement modules that are mentioned in requirements.txt
RUN pip install -r requirements.txt
#copy the current directory to /code/ directory
COPY . /code/
