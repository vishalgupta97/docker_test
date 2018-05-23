FROM ubuntu:16.04

# Update and install pip
RUN apt-get update -y && apt-get install -y python-pip

# Install flask
RUN pip install flask

# Copy code files
COPY . /app

# Change workdir
WORKDIR /app

# Expose port
EXPOSE 5000

# Run python
ENTRYPOINT ["python", "app.py"]
