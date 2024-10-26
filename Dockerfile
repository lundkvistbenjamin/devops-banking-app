# Base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY . .

# Command to run your app (replace with appropriate command for V1)
CMD ["python", "app/bank_app.py"]
