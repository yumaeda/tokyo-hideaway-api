# Setup

## 1. Install ansible

```bash
brew install ansible
```


## 2. Modify AWS configuration file
- Edit `./app/.aws_config.json` and specify below parameters:

```bash
{
    "access_key_id": "XXXXXXXX",
    "secret_access_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "region": "ap-northeast-1"
}
```


## 3. Modify vault password file
- Edit `./app/.vault_password` and replace XXXXXXX with your password.


## 4. Encrypt AWS configuration file.

```bash
ansible-vault encrypt ./app/.aws_config.json
```

&nbsp;


# How to Deploy

## 1. Edit app/models/config.py

- Set the below constants.

```python
SECRET_NAME = '<AWS Secret Name>'
```


## 2. Build an image

```bash
docker build -t yumaeda/kojinten .
```


## 3. Test locally

```bash
docker run -d --name kojinten_container -p 80:80 yumaeda/kojinten
```


## 4. Push the image to the Docker Hub

```bash
docker login
docker push yumaeda/kojinten:latest
```

&nbsp;

# References
[tiangolo/uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker) 

