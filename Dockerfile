FROM python:3.10.3-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH='/Plutus'

WORKDIR /Plutus
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -ms /bin/bash plutus_user \
    curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="${HOME}/.cargo/bin:${PATH}"
USER plutus_user
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /Plutus