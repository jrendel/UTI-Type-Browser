from ubuntu:14.04

run apt-get update

#run apt-get install -y build-essential git
#run apt-get install -y nginx supervisor

run apt-get install -y python
run apt-get install -y python-pip

run pip install vex

copy app /home/docker/app

workdir /home/docker/app

run pip install -r requirements.txt

expose 80

cmd ifconfig -a

entrypoint gunicorn -w 1 -b 0.0.0.0:80 app:app

# set IID (docker build --tag test --quiet .)
# set CID (docker run --detach -p 5000 $IID)
# docker inspect --format '{{ .NetworkSettings.IPAddress }}' $CID



# docker kill (docker ps --quiet)
