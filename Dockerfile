FROM python:3.11-slim

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
