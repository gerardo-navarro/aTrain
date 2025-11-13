# Use Python 3.11 as base image (3.10+ required)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
# These are needed for various Python packages and audio processing
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    g++ \
    ffmpeg \
    sox \
    libsox-dev \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    libgirepository1.0-dev \
    gir1.2-gtk-3.0 \
    && rm -rf /var/lib/apt/lists/*

# Copy all necessary files
COPY pyproject.toml MANIFEST.in ./
COPY aTrain ./aTrain

# Install Python dependencies in development mode
# This will install all dependencies listed in pyproject.toml
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -e .

# Expose Flask development server port
EXPOSE 5000

# Set environment variables for development
ENV FLASK_APP=aTrain.app
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

# Create directory for models
RUN mkdir -p /app/models

# Default command runs Flask in dev mode via aTrain CLI
CMD ["python", "-m", "aTrain", "dev"]
