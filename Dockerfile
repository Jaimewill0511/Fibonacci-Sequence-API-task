# Use slim base image for smaller size
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies early (cache better)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ app/
COPY app/main.py .

# Expose port
EXPOSE 8000

# Run using Gunicorn with 4 workers
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:create_app()"]
