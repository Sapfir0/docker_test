
FROM python:3.8-alpine

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["python", "app.py"]