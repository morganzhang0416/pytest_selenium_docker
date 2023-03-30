FROM seleniarm/standalone-chromium:latest
USER root
RUN apt-get update && \
    apt-get install -y python3-venv python3-pip
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /venv

