FROM python:3.11-slim

# Install netcat for the entrypoint script to check DB availability
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .


# Command to run the application
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

#ENTRYPOINT ["uvicorn", "app.main:app"]
#CMD ["--host", "0.0.0.0", "--port", "80"]


# Add entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]