# Stage 1: Build stage
FROM python:3.8-buster as build

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

# Copy all app files
COPY . .

# Install Python dependencies into a separate directory
RUN pip install --upgrade pip && \
    pip install --prefix=/install flask mysqlclient

# Stage 2: Final runtime image
FROM python:3.8-slim

WORKDIR /app

# Copy installed dependencies from build layer
COPY --from=build /install /usr/local

# Copy application source code only
COPY --from=build /app /app

EXPOSE 5002

CMD ["python", "app.py"]
