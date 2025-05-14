# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory to /app inside the container
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5555, the port your app will run on
EXPOSE 5555

# Command to run your application
CMD ["python", "your_microservice.py"]
