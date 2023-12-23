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
COPY detalles.py /

# final configuration
ENV FLASK_APP=detalles
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000
