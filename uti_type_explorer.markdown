aws ecr get-login --region us-east-1 | pbcopy
docker build -t uti_type_explorer .
docker tag uti_type_explorer:latest 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest
docker push 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest
