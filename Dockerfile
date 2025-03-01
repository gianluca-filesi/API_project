# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose the port that Render provides via the $PORT environment variable
EXPOSE $PORT

# Define the command to run your app using the shell script
CMD ["./start.sh"]
