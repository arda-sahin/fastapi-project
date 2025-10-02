FROM python:3.11-slim

# Install netcat for the entrypoint script to check DB availability
# RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt /requirements.txt
# Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app

# Add entrypoint script
# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]