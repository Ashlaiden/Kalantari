FROM python:3.11-slim

WORKDIR /app

# نصب dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# جمع‌آوری استاتیک و migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# اجرای gunicorn
CMD ["gunicorn", "Kalantari.wsgi:application", "--bind", "0.0.0.0:8000"]
