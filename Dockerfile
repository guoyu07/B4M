FROM python:3

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -Ue .

CMD python b4m/libs/encryptor.py
