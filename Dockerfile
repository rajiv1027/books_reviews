# Dockerfile

# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE jktech.settings

# Create and set the working directory
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# # Run Collectstatic
# RUN python manage.py collectstatic
# # Run migrations
# RUN python manage.py migrate

# Run migrations with option to retain existing data
RUN python manage.py migrate

# Run Collectstatic
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
