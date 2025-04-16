# Assignment 3: Docker Compose - Nginx + BusyBox Writer

This assignment demonstrates a multi-container Docker Compose setup where an Nginx server serves HTML updated every 5 seconds by a BusyBox writer container.

---

## ✅ Setup Overview

- **Nginx**: Serves content from `/usr/share/nginx/html` on port 8080.
- **BusyBox**: Writes an updated HTML file every 5 seconds to a shared volume.
- **Volume**: `shared-html` is mounted to both containers.
- **Network**: `shared-net` allows inter-container communication.

---

## 📄 docker-compose.yml Highlights

- Nginx container listens on **port 8080**
- HTML page auto-refreshes every **5 seconds**
- BusyBox generates the HTML content with a timestamp

---

## ▶️ How to Run

1. Navigate to the folder:
```bash
cd ~/docker-assignment-3
```

2. Start the services:
```bash
docker compose down
docker compose up -d
```

3. Open the app in your browser:
```
http://<EC2-PUBLIC-IP>:8080
```
#I have given my EC2 key which is http://51.21.243.46:8080 
You will see a web page that updates with the current time every 5 seconds.

---

## 🧠 Summary

- Used Docker Compose to run multiple containers with shared volumes and networks.
- Demonstrated inter-container communication and auto-generated HTML serving.
