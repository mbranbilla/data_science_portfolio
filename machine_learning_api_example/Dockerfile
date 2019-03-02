# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY requirements.txt dependencies.sh /

# Install any needed packages specified in requirements.txt
RUN sh dependencies.sh

# Install python requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Remove requirements files
RUN rm requirements.txt dependencies.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
## ENV NAME World

# Run app.py when the container launches
CMD ["python", "api.py"]
