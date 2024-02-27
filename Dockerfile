# Use an official Python runtime as a base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container at /app
COPY . .

# Expose the port the application runs on
EXPOSE 8080

# Define the command to run the application when the container starts
CMD ["python", "calculator.py"]
