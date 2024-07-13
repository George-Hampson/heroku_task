# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world (not necessary for Heroku, but good for local testing)
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV GITHUB_COMMIT_COUNT=${GITHUB_COMMIT_COUNT}

# Run the application
CMD flask run --host=0.0.0.0 --port=${PORT:-5000}
