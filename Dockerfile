FROM python:3

RUN pip install docker-py

COPY dit.py /
CMD ["python3", "/dit.py"]
