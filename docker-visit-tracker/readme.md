# Final Assignment: Dockerized Visit Tracker with Date Breakdown

This project demonstrates a FastAPI-based web application that records and displays timestamped visit logs. The backend is powered by MySQL, and Docker Compose is used for orchestration with data persistence and health checks.

---

## ✅ Features

- FastAPI app with endpoint `/` that:
  - Logs each visit with a UTC timestamp
  - Returns total number of visits
  - Returns a breakdown of visits grouped by date
- MySQL 8.0 database with named Docker volume
- Health check to ensure MySQL is up before FastAPI starts
- Custom Docker network for app and database
- Volume persistence for database data

---

## 🛠️ Project Structure

```
docker-visit-tracker/
├── app.py
├── Dockerfile
├── requirements.txt
└── docker-compose.yml
```

---

## ▶️ How to Run

1. Navigate to the project folder:
```bash
cd ~/docker-assignments/docker-visit-tracker
```

2. Build and run the containers:
```bash
docker compose up --build
```

3. Access the app in browser:
```
http://<EC2-PUBLIC-IP>:8080
```

4. To stop:
```bash
docker compose down
```

✅ Restarting with `docker compose up` again will retain visit data due to the named volume.

---

## 🖥️ Expected Output

```json
{
  "total_visits": 6,
  "breakdown": {
    "2025-04-15": 4,
    "2025-04-16": 2
  }
}
```

Each browser refresh inserts a new timestamped visit. Data is grouped by date using SQL.

---

## 🧠 Summary

- Used Docker Compose for full-stack orchestration
- Implemented service dependency via MySQL health check
- Demonstrated date-based data breakdown using SQL
- Maintained persistent data via Docker volume

This assignment showcases production-like container management for web applications with a database.
