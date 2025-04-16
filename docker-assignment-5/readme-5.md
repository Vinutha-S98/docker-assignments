# Assignment 5: Docker Custom Network & Container Communication

This assignment demonstrates Docker container communication across a custom bridge network, and isolation from the default network.

---

## ✅ Setup Overview

- Created a custom Docker network
- Launched 2 BusyBox containers in that network
- Verified they could ping each other by container name
- Launched a 3rd BusyBox container in the default network to show network isolation

---

## ▶️ Commands Used

```bash
# Create custom bridge network
docker network create my-custom-bridge

# Start 2 containers in that network
docker run -dit --name box1 --network my-custom-bridge busybox sh
docker run -dit --name box2 --network my-custom-bridge busybox sh

# Start 3rd container in default network
docker run -dit --name box3 busybox sh

# Test communication
docker exec -it box1 sh
ping box2   # ✅ Success

docker exec -it box3 sh
ping box1   # ❌ Fails (network isolation)
```

---

## 🧠 Summary

- Containers on the same custom network can resolve each other by name.
- Default and custom networks are isolated from each other.
- Demonstrates Docker networking fundamentals.
