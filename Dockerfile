FROM python:3.8.1-slim-buster

COPY . /app

RUN apt-get update \
&& apt-get install -y procps \
&& crontab /app/cronjob \
&& pip install -r /app/requirements.txt 

CMD bash /app/is_up.sh