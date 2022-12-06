FROM python:3.10-alpine

ADD requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /code

CMD sh
