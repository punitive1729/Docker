# Interact with container to provide some input

1. Use "docker run -i -t imageId"

"-i" means interactive mode setup for container
"-t" creates pseudo terminal for the container exposed for outside access

2. "docker start -a -i containerId/containerName"

"-a" means start container in attached mode
"-i" means start container in interactive mode
