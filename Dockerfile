FROM python:3.9-slim-buster

RUN apt-get update && apt-get clean

COPY requirements.txt ./
COPY . /app

RUN python3.9 -m pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

ENTRYPOINT ["python3", "/app/main.py"]
