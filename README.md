# uwsgi-nginx-flask

## Build an image:

```bash
docker build -t yumaeda/kojinten .
```

## Run a container based on the image:

```bash
docker run -d --name kojinten_container -p 80:80 yumaeda/kojinten
```

## Push the image to the Docker Hub.

```bash
docker login
docker push yumaeda/kojinten:latest
```

## References
[tiangolo/uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker) 

