FROM python:3

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

RUN pip install -Ue .

CMD python b4m/bin/run.py runserver
