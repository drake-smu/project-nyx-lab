FROM tensorflow/tensorflow:2.0.0-gpu-py3-jupyter
# RUN apt-get update -y && \
#     apt-get install -y flask \
#     ca-certificates build-essential
ARG username=semg
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
ENV DEBIAN_FRONTEND noninteractive
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER
# Install Python 3 packages
####################################################

# Install python3 and pip package manager
RUN pip install --upgrade pip 

COPY requirements.txt /app/

# WORKDIR /app

RUN pip install --no-cache-dir \
  -r /app/requirements.txt

# set directories and ports
####################################################
WORKDIR /app
RUN pwd
EXPOSE 8888
EXPOSE 8889
EXPOSE 81

# ENTRYPOINT ["python"]

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root

# CMD ["app.py"]
