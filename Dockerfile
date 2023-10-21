FROM python:slim
WORKDIR app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY templates ./templates
COPY *.py ./

CMD ["python", "server.py"]