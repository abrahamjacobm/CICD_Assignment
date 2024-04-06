# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container's working directory
COPY requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire project directory into the container's working directory
COPY train.py /code/train.py
COPY test.py /code/test.py

# Command to train the model during image build (optional)
# Adjust as needed based on your project structure and requirements
RUN python train.py

# Command to run the test script when the container starts
CMD ["python", "test.py"]
