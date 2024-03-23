FROM python:3.12.1

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/cache/apt/archives/*.deb

COPY . drf
WORKDIR /drf

RUN pip install -r requirements.txt && \
    python manage.py collectstatic --noinput && \
    python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
