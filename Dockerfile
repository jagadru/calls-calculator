FROM python:3.7-alpine

WORKDIR /usr/src/calls_calculator

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "run.py" ]
