FROM python:3.10.8-slim-bullseye
COPY mainFibo.py /app/
WORKDIR /app/
ENTRYPOINT ["python", "mainFibo.py"]


