FROM python:3.7-slim-buster
ENV DEBIAN_FRONTEND noninteractive

#get latest python
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y --no-install-recommends python3 python3-virtualenv python3-dev python3-pip

#get dependencies for the blender
RUN apt-get install -y --no-install-recommends libx11-6 libxi6 libxxf86vm1 libxfixes3 libxrender1

#get all other utilities
RUN apt-get install -y --no-install-recommends unzip wget bzip2 

#get the dependencies for the script
RUN mkdir -p /local/
RUN pip install requests pathlib

#get the blender 2.81a and setup the paths
RUN wget -q https://mirror.clarkson.edu/blender/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2
RUN tar xf blender-2.81a-linux-glibc217-x86_64.tar.bz2 -C /usr/bin/
#clean up
RUN rm blender-2.81a-linux-glibc217-x86_64.tar.bz2

#copy the shared lib for blender
RUN cp /usr/bin/blender-2.81a-linux-glibc217-x86_64/lib/lib* /usr/local/lib/
RUN ldconfig

# Entry point for dis.co
WORKDIR /local/
ENTRYPOINT ["python", "-u"]
