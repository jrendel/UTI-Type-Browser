aws ecr get-login --region us-east-1 | pbcopy
docker build -t uti_type_explorer .
docker tag uti_type_explorer:latest 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest
docker push 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest



http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html

eval (aws ecr get-login)
docker push 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest


# set IID (docker build --tag test --quiet .)
# set CID (docker run --detach -p 5000 $IID)
# docker inspect --format '{{ .NetworkSettings.IPAddress }}' $CID



# docker kill (docker ps --quiet)
