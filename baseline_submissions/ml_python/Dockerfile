FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

# ADITIONAL PYTHON DEPENDENCIES (if you have them)
COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /app

# COPY WHATEVER OTHER SCRIPTS YOU MAY NEED
COPY trained_model /trained_model
COPY submission.py utils.py ./
# SPECIFY THE ENTRYPOINT SCRIPT
CMD ["python", "-u", "submission.py"]