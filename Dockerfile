FROM ubuntu:12.04
MAINTAINER Alexander Balzer <abalzer22@gmail.com>

RUN apt-get update
RUN apt-get install python2.7 -y

RUN mkdir s9ace/
ADD src/ s9ace/

CMD ["ls -la"]
