# 7. Docker



<p align="center" > 
	<img src="./pics/docker02.png" width="25%" heigth="25%" />
</p>


[Docker](https://www.docker.com/) is probably the most popular system for running and deploying linux containers. What is a linux container???  It is a sort of "virtualization" where isolated Linux system can be run on a host system. We could say that a linux container is a lighter virtual machine.

Docker is very usefull when you want to deploy an app, you write your app, then you create a Dockerfile that contain commands that will assemble an OS with you app and configurations. This image can be deploy in a server

Docker ecosystem is very broad and  extensive documentation:

- [Container Tutorial](http://containertutorials.com/)

- [List of Docker resources](https://github.com/veggiemonk/awesome-docker)


The PyWPS-worshop will just briefelly touch the topic.

## Exercises

### 7.1. Dockerfiles

To build/generate a container image we need a Dockerfile, in folder `docker/` there are two options

```
flask/
nginx/
```


``flask/`` contains a Dockerfile with instructions to assemble a flask app implementation while ``nginx`` will implemente the stack PyWPS+Gunicorn+Nginx

Lets just see the `Dockerfile` from `flask/`, to create image names pywps4 from the local Dockerfile (.)

```
docker build -t pywps4 .
```

After build the image will be available to run

```
#to see images available
docker images

docker run -it -p5000:5000 pywps4:latest
```

On the browser the url `http://localhost:5000/wps` should point to a PyWPS running in a container. Please consult documentation for more docker information

**TIP**: You can pull an image from the dockerhub [repository](https://hub.docker.com/r/jorgedejesus/pywps4-demo/)


This was a very very brief example we recomment looking at geocontainer project for other osGEO images ([here](https://hub.docker.com/r/geocontainers/)) 

<p align="center" > 
	<img src="./pics/docker_animals.png" width="50%" heigth="50%" />
</p>
