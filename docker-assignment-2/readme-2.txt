# Assignment 2: Hello Docker App (Python + Environment Variable)

This assignment demonstrates how to build a simple Python application into a Docker image, then run it with and without an environment variable.

---

## ✅ Step-by-Step Instructions

### 🛠️ Step 1: Create the Project Structure
- Created a folder named `docker-assignment-2` and navigated into it.

### 📄 Step 2: Created the Python App
- Wrote a Python script (`app.py`) that prints a message using an environment variable.

### 🐳 Step 3: Created the Dockerfile
- Defined a base image, copied the script, and set a default command.

### 🔧 Step 4: Built the Docker Image
```bash
docker build -t hello-python-app-2 .
```

### ▶️ Step 5: Ran the Container (Default Behavior)
```bash
docker run hello-python-app-2
```
**Expected Output:**
```
Hello, Docker!
```

### 🌍 Step 6: Ran with Environment Variable
```bash
docker run -e NAME=world hello-python-app-2
```
**Expected Output:**
```
Hello, world!
```

---

## 📦 Summary
- Demonstrated Docker image build and execution.
- Showed how to pass environment variables to a container.
- Used `python:3.9-slim` as the base image.
