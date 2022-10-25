FROM python:3.7

RUN apt-get update

RUN mkdir /usr/src/coref
WORKDIR /usr/src/coref

COPY requirements.txt ./

RUN python3.7 -m pip install --no-cache-dir -r requirements.txt
RUN python3.7 -m spacy download en_core_web_sm

COPY . .

EXPOSE 8150

CMD python3.7 ./coref.py
