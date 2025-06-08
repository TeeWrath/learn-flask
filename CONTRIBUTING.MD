# CONTRIBUTING

## How to run the Dockerfile locally

#### Create docker image
```
docker build -t TAG_FOR_IMAGE .
```
---
#### Run the image as a container with volume
```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0"
```
---