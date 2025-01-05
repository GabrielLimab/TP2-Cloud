# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY client.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 52022

# Command to run the Flask server
CMD ["python", "client.py"]