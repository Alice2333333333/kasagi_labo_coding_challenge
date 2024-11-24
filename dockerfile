# Use the Ubuntu base image
FROM ubuntu:24.04

# Set a working directory in the container
WORKDIR /app

# Install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the Challenge B script into the container
COPY challenge_b.py .

# Create a directory for input/output files
RUN mkdir -p /app/data

# Expose the input/output directory to the host
VOLUME ["/app/data"]

# Default command to run Challenge B
CMD ["python3", "challenge_b.py", "generate_random_object.txt", "/app/data/processed_output.txt"]
