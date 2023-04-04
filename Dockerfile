FROM python:3.10

RUN mkdir -p /usr/src/PySportBot
COPY . /usr/src/PySportBot
WORKDIR /usr/src/PySportBot/bot

CMD ["bash", "install.sh"]