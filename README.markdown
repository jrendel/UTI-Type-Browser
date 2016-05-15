



http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html

# Build
docker build --tag uti_type_explorer --rm=true  .
# Login
eval (aws ecr get-login)
# Tag
docker tag uti_type_explorer:latest 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest
# Push
docker push 581150808077.dkr.ecr.us-east-1.amazonaws.com/uti_type_explorer:latest

https://www.calazan.com/docker-cleanup-commands/


# Kill all running containers
docker kill (docker ps --quiet)
# Delete all stopped containers (including data-only containers)
docker rm (docker ps -a -q)
# Delete all 'untagged/dangling' (<none>) images
docker rmi (docker images -q -f dangling=true)
#Delete ALL images
docker rmi $(docker images -q)

