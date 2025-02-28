FROM python:3.13.1
WORKDIR /fizzbuzz
COPY ./src /fizzbuzz
COPY requirements.txt /fizzbuzz
RUN pip install -r requirements.txt
CMD ["python", "app.py"]