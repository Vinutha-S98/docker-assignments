FROM python:3.9-slim

WORKDIR /app

# Install netcat (nc)
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY start.sh .

CMD ["./start.sh"]

