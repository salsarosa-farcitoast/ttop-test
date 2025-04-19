# Use the official Playwright image with Python
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Install Playwright browsers (already included in this base image, but good to be sure)
RUN playwright install --with-deps

# Run your app
CMD ["python", "connect-keep-active.py"]
