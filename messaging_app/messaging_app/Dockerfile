FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    && apt-get clean

RUN pip3 install mysqlclient

COPY . /app/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
