from ubuntu:latest

expose 80

run apt-get update
run apt-get install -y python
run apt-get install -y python-pip

copy . /home/docker
workdir /home/docker
run pip install -r requirements.txt

entrypoint gunicorn -w 4 -b 0.0.0.0:80 app:app
