# Dockerfile
FROM bitnami/spark:3.5.1

# Install Python and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy requirements.txt
COPY requirements.txt /tmp/requirements.txt

# Install Python packages
RUN pip3 install -r /tmp/requirements.txt


# Change back to the default user
USER 1001
