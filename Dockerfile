FROM python:3.9-slim-buster

# Install necessary packages
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    wget \
    unzip

# Download and install the latest version of ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -q https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin && \
    rm chromedriver_linux64.zip

# Set display environment variable to avoid "no display specified" error
ENV DISPLAY=:99

# Install pytest
RUN pip install pytest

# Copy project files to the container
COPY . /app
WORKDIR /app

# Run pytest
CMD ["pytest"]
