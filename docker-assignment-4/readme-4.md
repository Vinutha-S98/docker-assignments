# Assignment 4: FastAPI + MySQL Visit Counter (Docker Compose)

This assignment demonstrates how to run a FastAPI application with a MySQL database using Docker Compose, and persist database data using a bind mount.

---

## ✅ Project Highlights

- **FastAPI App**: Increments and displays a visit counter.
- **MySQL**: Stores the visit count in a table.
- **Bind Mount**: Ensures MySQL data is not lost across restarts.
- **Docker Compose**: Manages both services and their environment configurations.

---

## 🗂️ Services Setup

- **Python App**:
  - Built from a custom `Dockerfile` using `python:3.9-slim`
  - Uses environment variables: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
  - Starts with: `uvicorn app:app --host 0.0.0.0 --port 8080`

- **MySQL**:
  - Image: `mysql`
  - Environment variables: `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`
  - Data directory bind mounted to host to persist data

---

## ▶️ How to Run

1. Go to the project folder:
```bash
cd ~/docker-assignment-4
```

2. Start the services:
```bash
docker compose up -d
```

3. Visit in browser:
```
http://<EC2-PUBLIC-IP>:8080
```

You’ll see a JSON message showing the visit count.

4. Stop and restart:
```bash
docker compose down
docker compose up -d
```

✅ Visit count should be preserved due to bind mount.

---

## 🖥️ Expected Output

```json
{
  "message": "Visit count: 3"
}
```

Each refresh will increment the counter. The value persists even after restarting the containers.

---

## 🧠 Summary

- Demonstrated a multi-container setup with persistent MySQL storage.
- Showed environment variable configuration and service dependencies.
- Used FastAPI and MySQL to simulate a simple, stateful web app.
