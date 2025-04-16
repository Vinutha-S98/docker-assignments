# Assignment 1: Run Nginx on EC2 and Modify HTML Page

This assignment demonstrates how to run an `nginx:alpine` Docker container on an AWS EC2 instance and serve a custom HTML page using Docker.

---

## 🚀 Steps Followed

### ✅ 1. Launched an EC2 Instance
- **AMI Used**: Amazon Linux 2
- **Security Group** allowed:
  - HTTP (TCP port 80) from 0.0.0.0/0
  - SSH (TCP port 22) from My IP

### ✅ 2. Connected to EC2 via MobaXterm
```bash
# I used my own private key and EC2's public IP
#EC2-public-IP is 51.21.243.46
ssh -i "path/to/your-key.pem" ec2-user@<EC2-public-IP>

```

### ✅ 3. Installed Docker on EC2
```bash
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
# Logged out and logged back in
```

### ✅ 4. Ran the Nginx Container
```bash
docker run -d -p 80:80 --name my-nginx nginx:alpine
```

### ✅ 5. Accessed Nginx in Browser
Opened: "http://51.21.243.46"  
✅ Saw the default Nginx welcome page.

### ✅ 6. Modified the HTML Page
```bash
docker exec -it my-nginx sh
echo "Hello Docker" > /usr/share/nginx/html/index.html
exit
```

### ✅ 7. Confirmed in Browser
Refreshed the page → Now it shows:
```
Hello Docker
```

---

## 📄 Summary
- This was the first assignment to verify Docker and port exposure works correctly on an EC2 setup.
- Demonstrated basic container interaction (`docker exec`) and port mapping.
