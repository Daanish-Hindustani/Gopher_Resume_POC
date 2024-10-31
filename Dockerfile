# Use the official Python slim image
FROM python:3.11-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy requirements file and install dependencies
COPY ./requirements.txt .
RUN apt-get update -y && \
    apt-get install -y netcat-openbsd && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy entrypoint script and make it executable
COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

# Create a directory for media files
RUN mkdir -p /code/media

# Copy the rest of the application code
COPY . .

# Set the entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]
