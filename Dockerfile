# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code to the working directory
COPY . .

# Expose the port that the app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
