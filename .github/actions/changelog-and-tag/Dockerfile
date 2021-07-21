FROM python:3.9-slim

RUN apt-get update && apt-get install -y git
COPY changelog-and-tag.py /changelog-and-tag.py
ENTRYPOINT [ "python", "/changelog-and-tag.py" ]
