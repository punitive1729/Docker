# Container

# How to use

1. Use "docker build ." to build the image. We'll get imageId copy it

2. "docker -p 4000:3000 imageId" imageId we get from running above command. This command maps localhost:4000 -> 3000 port on container

3. When making a request on localhost:4000 we'll get appropriate reponse that container has been setup
