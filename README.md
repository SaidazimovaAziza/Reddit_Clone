##Install [Docker](https://download.docker.com/linux/ubuntu/dists/)

Open Terminal when the installer is done. Test your Docker installation with the --version flag:

##Checking docker version:

```bash
docker --version

Docker version 17.12.0-ce, build c97c6d6
```

## Build the app using docker

Create a file called Dockerfile, copy-and-paste the code into that file, and save it.

```bash
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```



Create requirements.txt and app.py:
from file requirement.txt we will intall pip libraries for python, app.py will contain code of our project.

requirements.txt

```bash
Flask
Redis
```

app.py

```bash
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

```


All three files should be in the same directory:

```bash
$ls
Dockerfile		app.py			requirements.txt
```

This creates a Docker image, which we’re going to name using the --tag option. 

```bash
docker build --tag=nameofimage .
```

Checking for builting image

```bash
$ docker image ls

REPOSITORY            TAG                 IMAGE ID
nameofimage         latest              326387cea398
```
After that we can run our app

```bash
docker run -p 4000:80 nameofimage
```

Checking from:

```bash
URL http://localhost:4000
```
##Tests:
to run test:

```bash
python test_name.py
```
test coverage:

```bash
coverage run test_name.py
```
```bash
coverage report 
```
my test coverage:

```bash
app.py 89%
test-requests.py :100%
```

