
# UTI-Type-Browser

Web based browser for Apple's Uniform Type Identifier (UTI). See http://en.wikipedia.org/wiki/Uniform_Type_Identifier for more.

You can see this running at http://uti.schwa.io/

## Is this all the UTI Types?

No. This is just a list of UTI types imported from /System/Library/CoreServices/CoreTypes.bundle/Contents/Info.plist on Mavericks. I'll be scanning applications for all UTI Types and adding them in later builds. I might even add a form to upload your own UTI information.




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

