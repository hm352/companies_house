FROM python:3.8.1-slim-buster

COPY . /app

RUN apt-get update \
&& apt-get install -y procps \
&& pip install -r /app/requirements.txt 

CMD bash /app/start.sh