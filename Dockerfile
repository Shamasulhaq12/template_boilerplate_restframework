# Base Image
FROM python:3.11

# Set working directory
WORKDIR /server

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libpq-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Pipfile and Pipfile.lock
COPY Pipfile* ./

# Install project dependencies using pipenv
RUN pip install --upgrade pip && \
    pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=coresite.settings

# Expose port 8000
EXPOSE 8000

# Run migrations and start server
CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
