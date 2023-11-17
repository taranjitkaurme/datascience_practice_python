# Use the official Python image as the base image
FROM python:3.11.6


RUN pip install pipenv


# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY Pipfile /app/

# Install any dependencies
RUN pipenv install

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 for Flask to listen on
EXPOSE 5000

# Define the command to run your application
CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]

