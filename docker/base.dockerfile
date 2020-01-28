FROM python:3.7-slim-buster
ENV DEBIAN_FRONTEND noninteractive

#get latest python & blender related dependencies
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils python3 python3-virtualenv \
python3-dev python3-pip libx11-6 libxi6 libxxf86vm1 libxfixes3 libxrender1 unzip wget bzip2 \
&& rm -rf /var/lib/apt/lists/*

#get the dependencies for the script
RUN mkdir -p /local/
RUN pip install requests pathlib

#get the blender 2.81a and setup the paths
RUN cd /tmp && wget -q https://mirror.clarkson.edu/blender/release/Blender2.81/blender-2.81a-linux-glibc217-x86_64.tar.bz2 \
&& tar xf /tmp/blender-2.81a-linux-glibc217-x86_64.tar.bz2 -C /usr/bin/ && rm -r /tmp/blender-2.81a-linux-glibc217-x86_64.tar.bz2

#copy the shared lib for blender
RUN cp /usr/bin/blender-2.81a-linux-glibc217-x86_64/lib/lib* /usr/local/lib/ && ldconfig

# Entry point for dis.co
WORKDIR /local/
ENTRYPOINT ["python", "-u"]
