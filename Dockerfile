FROM python:3.9.6-slim-buster

ADD . /usr/src/calls_calculator 
WORKDIR /usr/src/calls_calculator

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:3101", "server.app:wsgi", "--timeout", "1200"]
