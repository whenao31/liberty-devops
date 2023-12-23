# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && \
    apt-get install -y \
    libmariadb-dev \
    python3 \
    python3-pip
RUN pip install flask==2.3.* flask_cors mariadb

# install app
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# final configuration
ENV FLASK_APP=app/app_module.py
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000
