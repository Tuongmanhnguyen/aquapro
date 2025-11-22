# 1. Use Python 3.13 Slim (Small & Secure)
FROM python:3.13-slim

# 2. Set Environment Variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files
# PYTHONUNBUFFERED: Ensures logs are flushed immediately (important for Docker logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set Working Directory inside container
WORKDIR /app

# 4. Install Dependencies
# We copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the Backend Code
COPY backend /app/backend

# 6. Change context to the backend folder so manage.py is available
WORKDIR /app/backend

# 7. Create the media directory for image uploads
RUN mkdir -p media

# 8. Expose the port
EXPOSE 8000

# 9. Run Gunicorn
# "config.wsgi:application" points to backend/config/wsgi.py
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]