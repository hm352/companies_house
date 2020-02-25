# Intro #

Aim: Connect and store data from Comapnies House Data stream (https://stream.companieshouse.gov.uk/companies )

Requirements: Fault tolerance and Dockerization

# Project  Overview / Flow #
Docker container starts, runs start.sh. Within start.sh is an infinite 
loop that calls main.py.

The main.py function:
    1. Checks data folder for most recent data entry. if Data, retrieves timepoint from json else timepoint is None
    3. Logs process id log in /tmp/company_house.pid
    4. Connects to stream
    5. Checks stream 
    6. Saves data

because main is inside start.sh, even if the stream stops abruptly
it should be able to restart from the last data point it captured.

# Documentatiom  #
https://developer-specs.companieshouse.gov.uk/streaming-api/reference/company-information/stream?v=latest

# Usage #

```
$ docker build -t my-app .
$ docker run -e API_KEY=xxxx my-app
```
