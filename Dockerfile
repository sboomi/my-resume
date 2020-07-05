FROM python:3.7-slim-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt && export FLASK_APP=app.py

EXPOSE 5000

CMD ['flask','run']