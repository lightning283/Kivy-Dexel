FROM ubuntu:latest
COPY . /KivyDexel
COPY /config/liz /bin
RUN chmod 777 /bin/liz
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y xauth
RUN apt-get install -y dialog
CMD bash /KivyDexel/config/config.sh