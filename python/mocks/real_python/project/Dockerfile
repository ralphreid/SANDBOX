############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Alpine
############################################################

FROM python:alpine

# File Author / Maintainer
MAINTAINER Ralph

# Copy the application folder inside the container
ADD . /app

# Get pip to download and install requirements:
RUN pip install -r /app/requirements.txt

# Set the default directory where CMD will execute
WORKDIR /app