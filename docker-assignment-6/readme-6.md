# Assignment 6: Docker Hub Push & Pull

This assignment demonstrates how to build, tag, push, pull, and run Docker images using Docker Hub.

---

## 🐳 Docker Image Workflow

### ✅ Step 1: Build the Image
Build a local Docker image from `Dockerfile` and `app.py`:
```bash
docker build -t hello-python-app-2 .
```

### ✅ Step 2: Tag the Image for Docker Hub
Tag the image with your Docker Hub username:
```bash
docker tag hello-python-app-2 vinutha1998/hello-python-app-2:v1
```

### ✅ Step 3: Login to Docker Hub
```bash
docker login
```
> Use your Docker Hub username and a **personal access token** (not your GitHub password).

### ✅ Step 4: Push the Image
```bash
docker push vinutha1998/hello-python-app-2:v1
```

### ✅ Step 5: Remove the Local Image
```bash
docker rmi vinutha1998/hello-python-app-2:v1
```

### ✅ Step 6: Pull the Image Again
```bash
docker pull vinutha1998/hello-python-app-2:v1
```

### ✅ Step 7: Run the Image with Environment Variable
```bash
docker run -e NAME=Vinutha vinutha1998/hello-python-app-2:v1
```

---

## 🧠 Summary

- Successfully practiced tagging and uploading a Docker image to Docker Hub.
- Pulled and executed the image from another system (simulated by removing it locally).
- Used environment variables to customize output.

**Expected Output:**
```
Hello, Vinutha!
```
