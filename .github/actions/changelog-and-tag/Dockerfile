FROM python:3.9-slim

RUN apt-get update && apt-get install -y git
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY changelog-and-tag.py /changelog-and-tag.py
ENTRYPOINT [ "python", "/changelog-and-tag.py" ]
