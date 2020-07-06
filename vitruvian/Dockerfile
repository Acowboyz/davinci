FROM python:3.8.3

ENV PYTHONUNBUFFERED 1

RUN pip3 install uwsgi

# Create app directory
WORKDIR /usr/src/app

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000


# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#sort-multi-line-arguments
RUN apt-get update && apt-get install -y \
    gettext \
    vim

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy source code to working directory
COPY . .

# "set no compatible" is used to fix arrow keys error in vim insert mode
# timeout is in case for non-nullable fields input return to throw an error
# RUN timeout 30 yes | python manage.py compilemessages
