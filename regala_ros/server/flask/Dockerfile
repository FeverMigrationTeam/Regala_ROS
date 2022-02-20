FROM python:3
WORKDIR /app
ADD . /app
RUN apt-get install python-dev
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y default-mysql-client && apt-get install redis-server
CMD ["uwsgi", "uwsgi.ini"]
