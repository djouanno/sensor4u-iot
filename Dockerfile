FROM ubuntu:16.04

RUN apt-get update && apt-get -y install python3

RUN mkdir /var/app && \
    git clone https://github.com/djouanno/sensor4u-iot.git && \
    mv /var/app/cron /etc/cron.d/

RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log
