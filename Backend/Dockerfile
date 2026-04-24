# Use a slim Python image for efficiency
FROM python:3.11-slim

# Install system dependencies (needed for certain Python libraries)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port (Gunicorn will bind to this)
EXPOSE 8080

# Use Gunicorn as the production server
# Use Gunicorn as the production server
# Binds to 0.0.0.0 and port 8080 directly
CMD gunicorn --workers 3 --bind 0.0.0.0:${PORT:-8080} app:app