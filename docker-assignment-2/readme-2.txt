# Assignment 2: Hello Docker App (Python + Environment Variable)

This assignment demonstrates how to build a simple Python application into a Docker image, then run it with and without an environment variable.

---

## ✅ Step-by-Step Instructions

### 🛠️ Step 1: Create the Project Structure
```bash
mkdir hello-docker
cd hello-docker
```

### 📄 Step 2: Create the Python App
Create `app.py` with the following code:
```python
import os

# Get the NAME environment variable, default to 'Docker' if not set
name = os.getenv('NAME', 'Docker')
print(f"Hello, {name}!")
```

### 🐳 Step 3: Write the Dockerfile
Create `Dockerfile` with:
```Dockerfile
# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy your Python app into the container
COPY app.py .

# Define the default command
CMD ["python", "app.py"]
```

### 🔧 Step 4: Build the Docker Image
```bash
docker build -t hello-docker-app .
```

### ▶️ Step 5: Run the Container (Default Behavior)
```bash
docker run hello-docker-app
```
**Expected Output:**
```
Hello, Docker!
```

### 🌍 Step 6: Run with Environment Variable
```bash
docker run -e NAME=World hello-docker-app
```
**Expected Output:**
```
Hello, World!
```

---

## 📦 Summary
- Shows how to build a Docker image from a `Dockerfile`
- Uses `python:3.9-slim` as the base image
- Demonstrates how to pass environment variables into a Docker container
