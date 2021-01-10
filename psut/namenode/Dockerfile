FROM bde2020/hadoop-namenode:2.0.0-hadoop2.7.4-java8
COPY --from=python:3 / /
RUN apt-get update
RUN apt-get install inotify-tools -y
RUN mkdir /urban
RUN mkdir /urban/uploads

WORKDIR /psut_scripts
RUN  nohup bash auto-upload.sh </dev/null >/urban/logs.txt 2>&1 &


