# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements into the image
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Expose the port your app runs on (adjust if not 5000)
EXPOSE 5000

# Run the Flask app (adjust filename if needed)
CMD ["python", "app.py"]
