# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5010

ENTRYPOINT ["gunicorn", "app:app", "--bind", "0.0.0.0:5010", "--timeout", "5" ]

