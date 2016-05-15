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
