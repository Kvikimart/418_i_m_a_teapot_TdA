FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r tda_user && useradd -r -g tda_user tda_user

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=tda_user:tda_user . .

ENV PORT=8080
EXPOSE 8080

USER tda_user
ENTRYPOINT ["sh", "start.sh"]
