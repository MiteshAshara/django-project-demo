FROM python:3.10-slim AS base-system

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install OS-level dependencies and TA-Lib
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    wget curl gcc make libtool autoconf libffi-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*
# Optional: Upgrade pip/tools
RUN pip install --upgrade pip setuptools wheel


# stage-2

# Use the official Python image
FROM base-system

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt || \
    (echo "Error installing Django. Check requirements.txt for valid version." && exit 1)

# Copy the project files
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]