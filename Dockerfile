# Use the official Python 3.10 image as the base image
FROM python:3.12

ENV PYTHONUNBUFFERED 1

# Install Git
RUN apt-get update && apt-get install -y git


# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Expose the port that the Django development server will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
