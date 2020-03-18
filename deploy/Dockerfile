# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

RUN apt-get update && apt-get install gcc -y && apt-get clean

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y default-libmysqlclient-dev && rm -rf /var/lib/apt
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip3 install --trusted-host pypi.python.org --default-timeout=1000 -r deploy/requirements.txt
RUN pip3 install mysql-connector


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
RUN chmod +x start.sh
RUN chmod +x wait-for-mysql.sh
#CMD ./start.sh
CMD ["./wait-for-mysql.sh", "db", "./start.sh"]